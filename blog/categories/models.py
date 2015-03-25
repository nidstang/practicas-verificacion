from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=25)


class CategoryManager(models.Manager):
	def __init__(self, bd):
		self.bd = bd

	def save_category(self, category):
		return self.bd.save(category)

	def get_category_by_name(self, name):
		return self.bd.get(name)