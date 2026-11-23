from django.urls import path

from todos.views import TodoListCreateAPIView, TodoDetailAPIView, CategoryListAPIView

urlpatterns = [
    path('', TodoListCreateAPIView.as_view(), name='todo-list'),
    path('<int:pk>/', TodoDetailAPIView.as_view(), name='todo-detail'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
]