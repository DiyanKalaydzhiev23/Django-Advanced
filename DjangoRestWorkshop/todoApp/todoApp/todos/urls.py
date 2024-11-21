from django.urls import path
from todoApp.todos.views import TodoListCreateApiView, CategoriesListView, TodoDetailView

urlpatterns = [
    path('', TodoListCreateApiView.as_view(), name='todo-list-create'),
    path('<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('categories/', CategoriesListView.as_view(), name='category-list'),
]