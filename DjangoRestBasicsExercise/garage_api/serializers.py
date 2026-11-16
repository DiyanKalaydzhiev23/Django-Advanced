from rest_framework import serializers

from garage_api.models import Manufacturer, Car


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"