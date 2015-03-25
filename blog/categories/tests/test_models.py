import unittest
import mock
from django.utils import timezone
from categories.models import CategoryManager, Category


class CategoryModelTest(unittest.TestCase):

	def test_save_category(self):
		category = Category(name="Winter")

		m = mock.Mock()
		m.save.return_value = 1

		categoryManager = CategoryManager(m)
		id_last_category = categoryManager.save_category(category)

		self.assertEquals(id_last_category, 1)

	def test_get_category(self):
		m = mock.Mock()
		m.get.return_value = Category(name="Winter")

		categoryManager = CategoryManager(m)
		category = categoryManager.get_category_by_name(1)

		self.assertEquals(category.name, "Winter")