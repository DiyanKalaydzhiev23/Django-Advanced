from django.urls import path
from libraryApi.books import views

urlpatterns = [
    path('books/', views.ListBooksView.as_view(), name='books_list'),
    path('book/<int:pk>/', views.BookViewSet.as_view(), name='book_viewset'),
]