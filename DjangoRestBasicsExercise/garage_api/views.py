from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from garage_api.models import Manufacturer, Car
from garage_api.serializers import ManufacturerSerializer, CarSerializer


@api_view(["GET", "POST"])
def manufacturer_list_view(request):
    if request.method == "GET":
        manufacturers = Manufacturer.objects.all()
        serializer = ManufacturerSerializer(manufacturers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    serializer = ManufacturerSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def manufacturer_detail_view(request, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
    except Manufacturer.DoesNotExist as exc:
        raise Http404 from exc

    if request.method == "GET":
        serializer = ManufacturerSerializer(manufacturer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == "PUT":
        serializer = ManufacturerSerializer(instance=manufacturer, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_200_OK)

    if request.method == "PATCH":
        serializer = ManufacturerSerializer(instance=manufacturer, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_200_OK)

    if request.method == "DELETE":
        manufacturer.delete()
        return Response(status=HTTP_204_NO_CONTENT)



class CarListApiView(APIView):
    def apply_query_params(self, queryset, query_params):
        year = query_params.get('year')
        manufacturer_id = query_params.get('manufacturer_id')

        if year is not None:
            try:
                year = int(year)
            except (TypeError, ValueError) as exc:
                raise ValidationError({"year": "year must be an integer"})

            queryset = queryset.filter(year=year)

        if manufacturer_id is not None:
            try:
                manufacturer_id = int(manufacturer_id)
            except (TypeError, ValueError) as exc:
                raise ValidationError({"manufacturer_id": "manufacturer_id must be an integer"})

            queryset = queryset.filter(manufacturer_id=manufacturer_id)

        return queryset

    def get(self, request):
        cars = self.apply_query_params(Car.objects.all(), request.query_params)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CarDetailApiView(APIView):
    def get_object(self, pk):
        try:
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist as exc:
            raise Http404 from exc

    def get(self, request, pk):
        car = self.get_object(pk)
        serializer = CarSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        car = self.get_object(pk)
        serializer = CarSerializer(car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        car = self.get_object(pk)
        serializer = CarSerializer(car, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        car = self.get_object(pk)
        car.delete()
        return Response(status=status.HTTP_400_BAD_REQUEST)
