from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from libraryApi.accounts.serializers import RegisterSerializer

UserModel = get_user_model()

class RegisterApiView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = RegisterSerializer
