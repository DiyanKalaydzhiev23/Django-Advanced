from unittest.mock import patch
from django.test import TestCase

from forumApp.common.tasks import _send_mail


class TestSendEmailTask(TestCase):

    @patch('forumApp.common.tasks.send_mail')
    async def test__send_mail__calls_django_send_mail_func(self, mock_django_send_mail):
        await _send_mail(
            subject="Test subject",
            message="Test message",
            from_email="test@test.com",
            recipient_list=["test1@test.com"],
        )

        mock_django_send_mail.assert_called_once_with(
            subject="Test subject",
            message="Test message",
            from_email="test@test.com",
            recipient_list=["test1@test.com"],
        )
