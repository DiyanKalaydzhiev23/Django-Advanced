from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def bad_language_validator(value):
    bad_words = ["bad_word1", "bad_word2", "bad_word3"]

    for bad_word in bad_words:

        if bad_word.lower() in value.lower():
            raise ValidationError('The text contains bad language!')


@deconstructible
class BadLanguageValidator:

    def __init__(self, bad_words=None):
        if bad_words is None:
            self.bad_words = ["bad_word1", "bad_word2", "bad_word3"]
        else:
            self.bad_words = bad_words
        # can be done with getters and setters

    def __call__(self, value):
        for bad_word in self.bad_words:
            if bad_word.lower() in value.lower():
                raise ValidationError('The text contains bad language!')
