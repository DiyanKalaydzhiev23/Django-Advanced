from django.db import models


class Book(models.Model):
    title = models.CharField(
        max_length=30,
    )

    pages = models.PositiveIntegerField()

    description = models.TextField(
        max_length=100,
        default="",
    )

    author = models.ManyToManyField(
        to='Author',
        related_name='books',
    )

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(
        max_length=100,
    )

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(
        max_length=100,
    )

    established_year = models.PositiveIntegerField()

    location = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    description = models.TextField()

    book = models.ForeignKey(
        to=Book,
        on_delete=models.CASCADE,
    )







