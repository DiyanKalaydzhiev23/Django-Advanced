from django.db import models


class Book(models.Model):
    title = models.CharField(
        max_length=20,
    )

    pages = models.PositiveIntegerField()

    description = models.CharField(
        max_length=100,
    )

    authors = models.ManyToManyField(
        to='Author',
        related_name='books',
    )


class Author(models.Model):
    name = models.CharField(
        max_length=30,
    )


class Publisher(models.Model):
    name = models.CharField(
        max_length=30,
    )

    established_year = models.PositiveIntegerField()

    location = models.CharField(
        max_length=100,
    )


class Review(models.Model):
    description = models.TextField()

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
    )
