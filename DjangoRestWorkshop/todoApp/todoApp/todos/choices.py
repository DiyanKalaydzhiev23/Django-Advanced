from django.db import models

class StateChoices(models.TextChoices):
    DONE = 'Done', 'Done'
    NOT_DONE = 'Not done', 'Not done'
