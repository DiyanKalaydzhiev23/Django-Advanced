from django.urls import path
from common.views import HomeView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]