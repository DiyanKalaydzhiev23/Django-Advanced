from django.urls import path
from todos import views

urlpatterns = [
    path('', views.TodoListCreateApiView.as_view(), name='todo-list-create'),
    path('<int:pk>/', views.TodoDetailApiView.as_view(), name='todo-detail'),
    path('categories/', views.CategoriesListApiView.as_view(), name='category-list'),
]