from django.conf import settings
from django.db import models


class Note(models.Model):
    title = models.CharField(
        max_length=100,
    )

    body = models.TextField()

    owner = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notes',
    )

    class Meta:
        permissions = (
            ("publish_note", "Can publish a note"),
        )

    def __str__(self) -> str:
        return self.title
