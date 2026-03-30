from django.urls import path
from advertisement_center.views import index, create_commercial, refresh_slogan, task_monitor

app_name = 'advertisement_center'

urlpatterns = [
    path('', index, name='index'),
    path('commercials/new/', create_commercial, name='create'),
    path('commercials/<int:pk>/refresh-slogan/', refresh_slogan, name='refresh_slogan'),
    path('tasks/', task_monitor, name='tasks')
]
