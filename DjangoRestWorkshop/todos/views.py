from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateAPIView

from todos.filters import TodoFilter
from todos.models import Todo, Category
from todos.serializers import TodoSerializer, CategorySerializer, TodoNestedSerializer


class TodoListCreateApiView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filterset_class = TodoFilter


class TodoDetailApiView(RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoNestedSerializer


class CategoriesListApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer