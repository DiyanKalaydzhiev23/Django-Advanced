from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Category(models.Model):
    name = models.CharField(
        max_length=15
    )


class Todo(models.Model):
    class StateChoice(models.TextChoices):
        DONE = "Done", "Done"
        NOT_DONE = "Not done", "Not done"

    title = models.CharField(
        max_length=50,
    )
    description = models.TextField()
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        related_name='todos',
    )
    state = models.BooleanField(
        choices=[
            (True, StateChoice.DONE),
            (False, StateChoice.NOT_DONE),
        ],
        default=False,
    )
    assignees = models.ManyToManyField(
        to=UserModel,
        related_name='assignees_todos',
        blank=True,
    )

    def __str__(self) -> str:
        return self.title
