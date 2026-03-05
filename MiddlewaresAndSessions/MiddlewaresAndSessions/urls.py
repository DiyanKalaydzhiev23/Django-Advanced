"""
URL configuration for MiddlewaresAndSessions project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from MiddlewaresAndSessions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('choose-language/', views.choose_language, name='chose-language'),
    path('', views.home_page, name='home'),
    path('session-expiry/', views.session_expiry, name='session-expiry'),
    path('clear-session/', views.clear_session, name='clear-session'),
    path('flush-session/', views.flush_session, name='flush-session'),
    path('read-theme-cookie/', views.read_theme_cookie, name='read-theme-cookie'),
    path('set-theme-cookie/', views.set_theme_cookie, name='set-theme-cookie'),
    path('read-signed-cookie/', views.read_signed_cookie, name='read-signed-cookie'),
    path('set-signed-cookie/', views.set_signed_cookie, name='set-signed-cookie'),
]
