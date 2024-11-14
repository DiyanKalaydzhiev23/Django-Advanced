from django.core.serializers import serialize
from django.db.models import PositiveIntegerField
from django.http import JsonResponse
from django.views import View
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from libraryApi.books.models import Book
from rest_framework.decorators import api_view

from libraryApi.books.serializers import BookSerializer


# def list_books_view(request):
#     books = Book.objects.all()
#
#     context = {
#         'books': books,
#     }
#
#     return render(request, 'some_template.html', context)

# Option without rest_framework
# def list_books_view(request):
#     books = Book.objects.all()
#
#     context = {
#         'books': books,
#     }
#
#     return JsonResponse(context)  # TODO: parse the context to JSON


# For next time
# class ListBooksApiView(ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

@api_view(['GET', 'POST',])
def list_books_view(request):
    if request.method == "GET":
        books = Book.objects.all()

        serializer = BookSerializer(books, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListBooksView(APIView):  # APIView is tha base class same as View is at Django

    def get(self, request):
        books = Book.objects.all()

        serializer = BookSerializer(books, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@extend_schema(
    request=BookSerializer,
    responses={201: BookSerializer, 400: BookSerializer},
)
class BookViewSet(APIView):
    @staticmethod
    def get_object(pk):
        return get_object_or_404(Book, pk=pk)

    @staticmethod
    def serializer_valid(serializer):
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk: int):
        book = self.get_object(pk)
        serializer = BookSerializer(book)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk: int):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)

        return self.serializer_valid(serializer)

    def patch(self, request, pk: int):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data, partial=True)

        return self.serializer_valid(serializer)

    def delete(self, request, pk: int):
        book = self.get_object(pk)
        book.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
