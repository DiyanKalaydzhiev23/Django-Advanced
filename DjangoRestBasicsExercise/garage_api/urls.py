from django.urls import path
from garage_api import views


urlpatterns = [
    path('manufacturers/', views.manufacturer_list_view),
    path('manufacturer/<int:pk>/', views.manufacturer_detail_view),
    path('cars/', views.CarListApiView.as_view()),
    path('car/<int:pk>/', views.CarDetailApiView.as_view()),
]
