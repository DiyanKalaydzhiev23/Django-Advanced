from rest_framework import serializers
from books_api.models import Book



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Book