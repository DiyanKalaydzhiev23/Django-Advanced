from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, ListCreateAPIView

from todos.models import Category, Todo
from todos.serializers import CategorySerializer, TodoSerializer, TodoListCreateSerializer


class CategoriesListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TodoDetailView(RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoListCreateView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoListCreateSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)

        return queryset
