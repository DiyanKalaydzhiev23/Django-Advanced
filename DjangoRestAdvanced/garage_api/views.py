from django.contrib.auth import get_user_model
from django.db.models import Count, Min, Max
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from garage_api.models import Car, Manufacturer, Part
from garage_api.serializers import CarSerializer, PartSerializer, ManufacturerNestedReadSerializer, \
    ManufacturerSerializer, CarNestedReadSerializer, PartWriteSerializer


# TODO: move to utils
class ReadWriteSerializerMixin:
    SAFE_METHODS = ['GET']

    read_serializer = None
    write_serializer = None

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return self.read_serializer
        return self.write_serializer


class ListCreateCarApiView(ReadWriteSerializerMixin, ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Car.objects.select_related('manufacturer').prefetch_related('parts').all()
    read_serializer = CarNestedReadSerializer
    write_serializer = CarSerializer
    filterset_fields = ['verified', 'year']
    ordering_fields = ['year']


class RetrieveUpdateDestroyCarApiView(ReadWriteSerializerMixin, RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.select_related('manufacturer').prefetch_related('parts').all()
    read_serializer = CarNestedReadSerializer
    write_serializer = CarSerializer


class ListCreateManufacturerApiView(ReadWriteSerializerMixin, ListCreateAPIView):
    queryset = Manufacturer.objects.prefetch_related('cars', 'parts').all()
    read_serializer = ManufacturerNestedReadSerializer
    write_serializer = ManufacturerSerializer


class PartModelViewSet(ReadWriteSerializerMixin, ModelViewSet):
    queryset = Part.objects.all()
    read_serializer = PartSerializer
    write_serializer = PartWriteSerializer


class CarStatsView(APIView):
    def get(self, request: Request) -> Response:
        stats = Car.objects.aggregate(
            total_cars=Count('id'),
            oldest_year=Min('year'),
            newest_year=Max('year'),
        )
        return Response(stats, status=status.HTTP_200_OK)


class AdminDashboardView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request: Request) -> Response:
        User = get_user_model()
        data = {
            'users_count': User.objects.count(),
            'manufacturers_count': Manufacturer.objects.count(),
            'cars_count': Car.objects.count(),
            'parts_count': Part.objects.count(),
            'requested_by': request.user.username,
        }
        return Response(data=data, status=status.HTTP_200_OK)