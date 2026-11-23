from rest_framework import serializers

from accounts.serializers import UserSerializer
from todos.models import Category, Todo


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['id']


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'id',
            'title',
            'description',
            'state',
            'category',
            'assignees',
        ]
        read_only_fields = ['id']


class TodoNestedSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Todo
        fields = [
            'id',
            'title',
            'description',
            'state',
            'category',
            'assignees',
        ]
        read_only_fields = ['id', 'category']

    def to_representation(self, instance) -> dict:
        data = super().to_representation(instance)
        data['assignees'] = UserSerializer(instance.assignees.all(), many=True).data
        return data
