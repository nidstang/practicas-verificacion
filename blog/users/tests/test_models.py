import unittest
import mock
from django.utils import timezone
from users.models import User


class UsersModelTest(unittest.TestCase):

	def test_str_method(self):
		user = User(username="pablo", firstname="Pablo", lastname="Fernandez", password="1234", age=19)
		self.assertEqual(user.__str__(), "Pablo Fernandez")