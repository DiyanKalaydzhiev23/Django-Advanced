from django.urls import path, include
from books_api import views
from books_api.views import ListBookView

urlpatterns = [
    path('books/', ListBookView.as_view()),
    path('book/', include([
        path('', views.create_book, name='create-book'),
        path('<int:pk>/', views.BookViewSet.as_view(), name='book'),
    ]))
]