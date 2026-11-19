from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from garage_api.mixin import ReadWriteSerializerMixin
from garage_api.models import Manufacturer, Car, Part
from garage_api.serializers import ManufacturerSerializer, CarSerializer, CarNestedReadSerializer, \
    ManufacturerNestedReadSerializer, PartSerializer, PartWriteSerializer


class ManufacturerListCreateAPIView(ReadWriteSerializerMixin, ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Manufacturer.objects.prefetch_related('cars', 'parts').all()
    read_serializer = ManufacturerNestedReadSerializer
    write_serializer = ManufacturerSerializer


class ManufacturerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class CarListCreateApiView(ReadWriteSerializerMixin, ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Car.objects.select_related('manufacturer').prefetch_related('parts').all()
    read_serializer = CarNestedReadSerializer
    write_serializer = CarSerializer
    filterset_fields = ['year', 'id']
    ordering_fields = ['year']


class CarRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class PartModelViewSet(ReadWriteSerializerMixin, ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Part.objects.all()
    read_serializer = PartSerializer
    write_serializer = PartWriteSerializer
