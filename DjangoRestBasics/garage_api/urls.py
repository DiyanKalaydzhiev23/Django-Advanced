from django.urls import path
from garage_api import views

urlpatterns = [
    path('manufacturers/', views.ListManufacturerApiView.as_view(), name='manufacturers-list'),
    path('cars/', views.ListCarApiView.as_view(), name='cars-list'),
    path('cars/stats/', views.CarStatsView.as_view(), name='cars-stats'),
    path('cars/<int:pk>/', views.CarDetailApiView.as_view(), name='car-detail'),
]
