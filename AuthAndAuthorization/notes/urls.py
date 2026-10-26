from django.urls import path
from notes import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home')
]