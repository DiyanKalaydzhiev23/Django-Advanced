from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter
from garage_api import views


router = SimpleRouter()
router.register('parts', views.PartModelViewSet, basename='parts')


urlpatterns = [
    path('cars/', include([
        path('', views.ListCreateCarApiView.as_view(), name='car-list'),
        path('<int:pk>/', views.RetrieveUpdateDestroyCarApiView.as_view(), name='car-detail'),
        path('stats/', views.CarStatsView.as_view(), name='car-stats'),
    ])),
    path('manufacturers/', views.ListCreateManufacturerApiView.as_view(), name='manufufacturer-list'),
    path('admin-dashboard/', views.AdminDashboardView.as_view(), name='admin-dashboard')
] + router.urls