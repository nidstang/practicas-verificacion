from django.db import models

class User(models.Model):
	username 	= models.CharField(max_length=8)
	firstname 	= models.CharField(max_length=25)
	lastname 	= models.CharField(max_length=35)
	password 	= models.CharField(max_length=16)
	age 		= models.IntegerField(default=0)

	def __str__(self):
		return self.firstname + " " + self.lastname
