from django.contrib.auth import get_user_model
from django.db import models

from forumApp.posts.choices import LanguageChoice
from forumApp.posts.validators import BadLanguageValidator, bad_language_validator


UserModel = get_user_model()

class Post(models.Model):
    TITLE_MAX_LENGTH = 100

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    content = models.TextField(
        validators=(
            BadLanguageValidator(),
        )
    )

    author = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    approved = models.BooleanField(
        default=False,
    )

    languages = models.CharField(
        max_length=20,
        choices=LanguageChoice.choices,
        default=LanguageChoice.OTHER,
    )

    image = models.ImageField(
        upload_to='post_images/',
        blank=True,
        null=True,
    )

    class Meta:
        permissions = [
            ('can_approve_posts', 'Can approve posts'),
        ]

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    author = models.CharField(
        max_length=100,
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

