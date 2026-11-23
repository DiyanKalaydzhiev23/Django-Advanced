from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, \
    TokenRefreshView, TokenBlacklistView
from accounts.views import UserCreationView, UserListAPIView

urlpatterns = [
    path('register/', UserCreationView.as_view(), name='user-create'),
    path('users/', UserListAPIView.as_view(), name='users-list'),  # TODO: fix the endpoints names so that they are more restful
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
]