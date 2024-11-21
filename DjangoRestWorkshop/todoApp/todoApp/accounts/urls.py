from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from todoApp.accounts.views import RegisterView, LoginView, LogoutApiView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutApiView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh-token')
]