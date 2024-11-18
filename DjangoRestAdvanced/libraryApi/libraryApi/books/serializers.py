from rest_framework import serializers
from django import forms

from libraryApi.books.models import Book, Author, Publisher


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']


class BookSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        authors = validated_data.pop('author')
        authors_names = [a['name'] for a in authors]
        # [{"name": "Dido"}, "name": "Pesho"] -> ["Dido", "Pesho"]

        book = Book.objects.create(**validated_data)  # no relation at this point

        existing_authors = Author.objects.filter(name__in=authors_names)
        existing_authors_names = set(existing_authors.values_list('name', flat=True))
        #  {'Dido'}

        new_authors_names = set(authors_names) - existing_authors_names
        # {"Pesho"}  get all new authors that have to be created

        new_authors = [Author(name=a_name) for a_name in new_authors_names]
        created_authors = Author.objects.bulk_create(new_authors)

        all_authors = list(existing_authors) + list(created_authors)
        # [<AuthorObj: Dido>, <AuthorObj: Pesho>]

        book.author.set(all_authors)

        return book


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"


class PublisherHyperlinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'
