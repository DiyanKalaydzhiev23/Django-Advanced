from django.db import models


class TodoStateChoice(models.TextChoices):
    DONE = "Done", "Done"
    NOT_DONE = "Not done", "Not done"
