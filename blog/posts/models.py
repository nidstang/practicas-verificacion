from django.db import models
from django.utils import timezone

class Post(models.Model):
	title 			= models.CharField(max_length=250)
	created_date 	= models.DateTimeField('date plublished')
	author 			= models.CharField(max_length=15)
	content			= models.CharField(max_length=1024)


class PostManager(models.Manager):

	def __init__(self, bd):
		self.bd = bd

	def get_by_author(self, author):
		self.filter(author=author)

	def save_post(self, post):
		return self.bd.save(post)

	def get_post_by_id(self, id_post):
		return self.bd.get(id_post)
