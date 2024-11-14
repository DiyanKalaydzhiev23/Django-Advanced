from rest_framework import serializers
from django import forms

from libraryApi.books.models import Book


# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = '__all__'
#

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
