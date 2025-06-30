from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

UserModel = get_user_model()

class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, email=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(email__iexact=email) | Q(username__iexact=username))
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password) and self.user_can_authenticate(user):
            return user

        return None
