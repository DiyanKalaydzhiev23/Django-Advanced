from django.urls import path
from notes import views

app_name = 'notes'

urlpatterns = [
    path('', views.NoteListView.as_view(), name='list'),
    path('<int:pk>/', views.NoteDetailView.as_view(), name='detail'),
]