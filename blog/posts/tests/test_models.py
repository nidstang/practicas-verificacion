import unittest
import mock
from django.utils import timezone
from posts.models import PostManager, Post


class PostModelTest(unittest.TestCase):
	def test_filter_by_author(self):
		author = mock.Mock()
		manager = mock.Mock(spec=PostManager)
		PostManager.get_by_author(manager, author)
		manager.filter.assert_called_with(author=author)


	def test_save_post(self):
		post = Post(title="A title", created_date=timezone.now(), author="Pablo", content="sss")

		m = mock.Mock()
		m.save.return_value = 1

		postManager = PostManager(m)
		id_last_post = postManager.save_post(post)

		self.assertEquals(id_last_post, 1)

	def test_get_post(self):
		m = mock.Mock()
		m.get.return_value = Post(title="A title", created_date=None, author="Pablo", content="sss")

		postManager = PostManager(m)
		post = postManager.get_post_by_id(1)

		self.assertEquals(post.title, "A title")