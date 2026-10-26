from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accounts import views

urlpatterns = [
    path('fbv/login/', views.login_fbv, name='fbv-login'),
    path('fbv/logout/', views.logout_fbv, name='fbv-logout'),
    path('fbv/register/', views.register_fbv, name='fbv-register'),
    path('cbv/login/', LoginView.as_view(), name='cbv-login'),
    path('cbv/logout/', LogoutView.as_view(), name='cbv-logout'),
]
