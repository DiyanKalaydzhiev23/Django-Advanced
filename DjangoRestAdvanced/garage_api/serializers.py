from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from garage_api.models import Manufacturer, Car, Part


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part
        fields = "__all__"


class ManufacturerNestedReadSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)
    parts = PartSerializer(many=True, read_only=True)

    class Meta:
        model = Manufacturer
        fields = "__all__"


class CarNestedReadSerializer(serializers.ModelSerializer):
    manufacturer = ManufacturerSerializer(read_only=True)
    parts = PartSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = '__all__'



class PartManufacturerWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = (
            'id',
            'name',
            'country',
            'founded_year',
        )
        extra_kwargs = {
            'name': {'required': False, 'allow_null': True, 'allow_blank': True},
            'country': {'required': False, 'allow_null': True, 'allow_blank': True},
        }

    def validate(self, attrs):
        manufacturer_id = self.parent.initial_data['manufacturer'].get('id')

        if manufacturer_id is not None:
            try:
                attrs['manufacturer_instance'] = Manufacturer.objects.get(pk=manufacturer_id)
            except Manufacturer.DoesNotExist as exc:
                raise ValidationError({'id': 'Manufacturer with this id doesn\'t exist'})

            return attrs

        manufacturer_serializer = ManufacturerSerializer(data=attrs)
        manufacturer_serializer.is_valid(raise_exception=True)
        attrs['manufacturer_data'] = manufacturer_serializer.validated_data
        return attrs

"""
{
name: Turbo,
price: 1000,
manufacturer: {'name': '...', 'country': '...'}
manufacturer: {'id': 1}
}
"""

class PartWriteSerializer(serializers.ModelSerializer):
    manufacturer = PartManufacturerWriteSerializer()

    class Meta:
        model = Part
        fields = '__all__'

    @staticmethod
    def resolve_manufacturer(data):
        manufacturer = data.get('manufacturer_instance')

        if manufacturer:
            return manufacturer

        return Manufacturer.objects.create(**data.get('manufacturer_data'))

    def create(self, validated_data: dict):
        manufacturer_data = validated_data.pop('manufacturer')
        cars = validated_data.pop('cars', [])

        part = Part.objects.create(
            manufacturer=self.resolve_manufacturer(manufacturer_data),
            **validated_data
        )

        if cars:
            part.cars.set(cars)

        return part

    def update(self, instance, validated_data):
        manufacturer_data = validated_data.pop('manufacturer')
        cars = validated_data.pop('cars', [])

        if manufacturer_data is not None:
            instance.manufacturer = self.resolve_manufacturer(manufacturer_data)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if cars:
            instance.cars.set(cars)

        return instance
