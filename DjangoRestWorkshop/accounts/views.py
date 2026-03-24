from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, ListAPIView

from accounts.serializers import UserSerializer


UserModel = get_user_model()


class UserCreationView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class UserListApiView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer