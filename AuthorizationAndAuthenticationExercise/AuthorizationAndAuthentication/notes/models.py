from django.db import models
from django.conf import settings


class Note(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notes",
    )

    title = models.CharField(
        max_length=100,
    )

    body = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self) -> str:
        return f"{self.title} ({self.owner.username})"
