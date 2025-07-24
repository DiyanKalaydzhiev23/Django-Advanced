from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.test import TestCase
from django.urls import reverse

from forumApp.posts.models import Post

UserModel = get_user_model()


class TestApprovePostView(TestCase):
    def setUp(self):
        self.user_credentials = {
            "username": "test",
            "email": "test@test.com",
            "password": "12test34",
        }

        self.user = UserModel.objects.create_user(
            **self.user_credentials
        )

        self.post = Post.objects.create(
            title="Test",
            content="That's some content right here",
            approved=False,
            author=self.user,
        )

        self.client.login(
            email=self.user_credentials["email"],
            password=self.user_credentials["password"]
        )

    def test__approve_valid_post__approves_the_post_and_redirects(self):
        # Act
        response = self.client.post(
            reverse('approve', args=[self.post.pk]),
            HTTP_REFERER=reverse('index')
        )

        self.post.refresh_from_db()

        # Assert
        self.assertRedirects(response, reverse('index'))
        self.assertTrue(self.post.approved)

    def test__approve_invalid_post__raises_DoesNotExist_error(self):
        with self.assertRaises(self.post.DoesNotExist) as dne:
            self.client.post(
                reverse('approve', args=[999]),
                HTTP_REFERER=reverse('index')
            )

        self.assertTrue(str(dne))