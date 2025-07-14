from django.urls import path, include
from rest_framework.routers import DefaultRouter

from books_api import views
from books_api.views import ListBookView, PublisherViewSet

router = DefaultRouter()
router.register(r'', PublisherViewSet)

urlpatterns = [
    path('books/', ListBookView.as_view()),
    path('book/', include([
        path('', views.create_book, name='create-book'),
        path('<int:pk>/', views.BookViewSet.as_view(), name='book'),
    ])),
    path('publisher/', include(router.urls)),
    path('publisher-links/', views.PublisherHyperLinkView.as_view(), name='publisher-links')
]