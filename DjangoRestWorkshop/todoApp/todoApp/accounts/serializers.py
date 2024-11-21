from django.contrib.auth import get_user_model
from rest_framework import serializers


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Not returned in the response

    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        # We do this in order to hash the password
        return user


class LoginRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class LoginResponseSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()
    message = serializers.CharField()


class LogoutRequestSerializer(serializers.Serializer):
    refresh = serializers.CharField()


class LogoutResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
