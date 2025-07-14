from rest_framework import serializers
from books_api.models import Book, Author, Publisher


class AuthorSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["name"]
        model = Author


class BookSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Book


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSimpleSerializer(many=True)  # read_only=True

    class Meta:
        fields = "__all__"
        model = Book

    def create(self, validated_data: dict):
        authors = validated_data.pop('authors')  # [{"name": "dido"}, ...]
        authors_names = [a.get('name') for a in authors]  # ["dido", ...]

        """
        validated_data = {
            "title": "Some book",
            "pages": 200,
            "description": "Book by Softuni"
        }
        """
        book = Book.objects.create(**validated_data)

        existing_authors = Author.objects.filter(name__in=authors_names)  # [<Author object in mem>, ...]
        new_author_names = (
            set(authors_names)  # ["Dido", "Nakov"]
                -
            set(existing_authors.values_list('name', flat=True))  # ["Nakov"]
        )  # ("Dido",)

        new_authors = [Author(name=name) for name in new_author_names]
        created_authors = Author.objects.bulk_create(new_authors)

        all_authors = list(existing_authors) + list(created_authors)
        book.authors.set(all_authors)

        return book


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"



class PublisherHyperlinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"
