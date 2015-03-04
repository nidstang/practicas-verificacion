from unittest import TestCase
from classes.posts import Posts

__author__ = 'pablo'


class TestPosts(TestCase):
    def test_create_post_category_doesnt_exists(self):
        self.assertRaises(ValueError, Posts.create_post, 'lie', 'test content')

    def test_create_post_content_as_html(self):
        self.assertRaises(RuntimeError, Posts.create_post, 'code', '<body>')

    def test_create_post_insert_ok(self):
        result = Posts.create_post("code", "test test test")
        assert result

    def test_delete_post_id_doesnt_exists(self):
        self.assertRaises(ValueError, Posts.delete_post, 98)

    def test_get_post_doesnt_exists(self):
        self.assertRaises(ValueError, Posts.get_post, 98)

    def test_get_post_test(self):
        result = Posts.get_post(1)
        self.assertEquals(result, "entradadeprueba")



