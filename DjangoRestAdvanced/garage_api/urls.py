from django.urls import path
from rest_framework.routers import SimpleRouter

from garage_api import views


router = SimpleRouter()
router.register('parts', views.PartModelViewSet, basename='parts')


urlpatterns = [
    path('manufacturers/', views.ManufacturerListCreateAPIView.as_view(), name='manufacturer-list'),
    path('manufacturer/<int:pk>/', views.ManufacturerRetrieveUpdateDestroyAPIView.as_view()),
    path('cars/', views.CarListCreateApiView.as_view()),
    path('car/<int:pk>/', views.CarRetrieveUpdateDestroyAPIView.as_view()),
] + router.urls
