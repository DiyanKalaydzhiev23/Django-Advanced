from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from accounts import views

urlpatterns = [
    path('login/', ObtainAuthToken.as_view(), name='login'),
    path('check-token/', views.check_token, name='check-token'),
]