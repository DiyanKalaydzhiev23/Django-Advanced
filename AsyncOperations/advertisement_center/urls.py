from django.urls import path
from advertisement_center.views import create_commercial, index, refresh_slogan, task_monitor

app_name = 'advertisement_center'

urlpatterns = [
    path('', index, name='index'),
    path('commercials/new/', create_commercial, name='create'),
    path('tasks/', task_monitor, name='tasks'),
    path('commercials/<int:pk>/refresh-slogan/', refresh_slogan, name='refresh_slogan'),
]