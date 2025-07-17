from rest_framework import serializers

from todos.models import Category, Todo


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only = ['id']


class BaseTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"


class TodoSerializer(BaseTodoSerializer):
    category = CategorySerializer(read_only=True)

    class Meta(BaseTodoSerializer.Meta):
        read_only = ['id', 'categories']


class TodoListCreateSerializer(BaseTodoSerializer):
    class Meta(BaseTodoSerializer.Meta):
        read_only = ['id']
