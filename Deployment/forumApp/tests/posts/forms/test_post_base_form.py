from django.test import TestCase
from forumApp.posts.forms import PostBaseForm
from forumApp.posts.models import Post


class TestPostBaseForm(TestCase):

    def setUp(self):
        self.valid_data = {
            'title': 'Valid title',
            'content': 'This is the content',
            'languages': 'py',
            'image': None,
        }

    def test__form_is_valid__expect_true(self):
        form = PostBaseForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test__empty_title__returns_error(self):
        self.valid_data['title'] = ''
        form = PostBaseForm(data=self.valid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test__title_too_long__returns_error(self):
        self.valid_data['title'] = 'a' * (Post.TITLE_MAX_LENGTH + 1)
        form = PostBaseForm(data=self.valid_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test__content_contains_title__returns_error(self):
        self.valid_data['title'] = 'a'
        self.valid_data['content'] = 'abcd'
        form = PostBaseForm(data=self.valid_data)
        self.assertFalse(form.is_valid())
        self.assertIsNotNone(form.errors)

    def test__save_method_capitalizes_title__expect_valid(self):
        self.valid_data['title'] = 'hello'
        form = PostBaseForm(
            data=self.valid_data
        )
        self.assertTrue(form.is_valid())

        post = form.save(commit=False)

        self.assertEqual(
            post.title,
            self.valid_data['title'].capitalize(),
        )