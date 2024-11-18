from django.contrib import admin
from libraryApi.books.models import Book
from unfold.admin import ModelAdmin



@admin.register(Book)
class BookAdmin(ModelAdmin):
    pass
