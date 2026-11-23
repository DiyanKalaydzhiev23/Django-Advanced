from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser

from accounts.serializers import UserSerializer


UserModel = get_user_model()


class UserCreationView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserListAPIView(ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer