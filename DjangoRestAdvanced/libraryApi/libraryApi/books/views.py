from django.core.serializers import serialize
from django.db.models import PositiveIntegerField
from django.http import JsonResponse
from django.views import View
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListAPIView, get_object_or_404, RetrieveAPIView, RetrieveUpdateDestroyAPIView, \
    ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from libraryApi.books.models import Book, Publisher
from rest_framework.decorators import api_view

from libraryApi.books.permissions import IsBookOwner
from libraryApi.books.serializers import BookSerializer, PublisherHyperlinkSerializer, PublisherSerializer, \
    BookSimpleSerializer


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


class ListBooksView(ListCreateAPIView):  # APIView is tha base class same as View is at Django
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


@extend_schema(
    request=BookSerializer,
    responses={201: BookSerializer, 400: BookSerializer},
)
class BookViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSimpleSerializer
    permission_classes = [IsAuthenticated, IsBookOwner]
    authentication_classes = [TokenAuthentication]


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherHyperlinkView(ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherHyperlinkSerializer










