from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from rest_framework import status, views, generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response

from books_api.models import Book, Publisher
from books_api.permissions import IsAuthor
from books_api.serializers import BookSerializer, BookSimpleSerializer, PublisherSerializer, \
    PublisherHyperlinkSerializer


# def book(request, pk: int):
#     book = Book.objects.get(pk=pk)
#
#     return JsonResponse({
#         "title": book.__dict__.get('title'),
#         "pages": book.__dict__.get('pages'),
#     })

class ListBookView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()  # better do this for N+1 problem -> prefetch_related('authors')


class BookViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSimpleSerializer
    queryset = Book.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthor]


    # def get_object(self, pk):
    #     return get_object_or_404(Book, pk=pk)
    #
    # def get(self, request, pk):
    #     book = self.get_object(pk)
    #     serializer = self.serializer(book)
    #     return Response(
    #         data=serializer.data,
    #         status=status.HTTP_200_OK
    #     )
    #
    # def put(self, request, pk):
    #     book = self.get_object(pk)
    #     serializer = self.serializer(
    #         instance=book,
    #         data=request.data
    #     )
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(
    #         data=serializer.data,
    #         status=status.HTTP_200_OK,
    #     )
    #
    # def patch(self, request, pk):
    #     book = self.get_object(pk)
    #     serializer = self.serializer(
    #         instance=book,
    #         data=request.data,
    #         partial=True,
    #     )
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(
    #         data=serializer.data,
    #         status=status.HTTP_200_OK,
    #     )
    #
    # def delete(self, request, pk):
    #     book = self.get_object(pk)
    #     book.delete()
    #     return Response(
    #         status=status.HTTP_200_OK,
    #     )






# @api_view(['GET'])
# def get_book(request, pk: int):
#     book = Book.objects.get(pk=pk)
#     serializer = BookSerializer(book)
#     return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(
        data=serializer.data,
        status=status.HTTP_201_CREATED
    )


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class PublisherHyperLinkView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherHyperlinkSerializer


"""
MPA:
    book/details/<int:pk>/ - GET 
    book/list/             - GET
    book/edit/<int:pk>/    - POST
    book/delete/<int:pk>/  - POST

REST API:
    books/                 - GET   - Returns a list of books
    books/<int:pk>/        - GET, PUT, PATCH, DELETE
    book/                  - POST 
"""

