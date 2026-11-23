from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView
from todos.models import Todo, Category
from todos.serializers import TodoSerializer, TodoNestedSerializer, CategorySerializer


class TodoListCreateAPIView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filterset_fields = ['category']


class TodoDetailAPIView(RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoNestedSerializer


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
