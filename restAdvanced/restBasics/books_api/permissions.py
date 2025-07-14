from rest_framework.permissions import BasePermission

from books_api.models import Book


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj: Book):
        authors_usernames = [n.lower() for n in obj.authors.values_list('name', flat=True)]
        return request.user.username.lower() in authors_usernames