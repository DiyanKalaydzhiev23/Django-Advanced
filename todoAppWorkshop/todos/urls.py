from django.urls import path
from todos.views import CategoriesListView, TodoDetailView, TodoListCreateView

urlpatterns = [
    path('', TodoListCreateView.as_view(), name='todo-list-create'),
    path('<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('categories/', CategoriesListView.as_view(), name='category-list'),
]