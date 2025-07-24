from django.core.exceptions import ValidationError
from django.test import TestCase

from forumApp.posts.validators import BadLanguageValidator


class TestBadLanguageValidator(TestCase):
    def setUp(self):
        self.bad_words = [
            "bad_1",
            "really_bad_2",
        ]

        self.validator = BadLanguageValidator(self.bad_words)

    def test__validate_clean_message__expect_success(self):
        self.validator("Clean message")

    def test__validate_explicit_content_message__expect_validation_error(self):
        with self.assertRaises(ValidationError) as ve:
            self.validator(self.bad_words[0] + "some text")

        self.assertTrue(str(ve))