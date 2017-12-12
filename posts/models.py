from django.contrib.auth.models import User
from django.db import models



class Category(models.Model):
	name = models.CharField(max_length=100, help_text="Category for the Bucketlist (e.g. Travel, Milestone, Skills")

	def __str__(self):
		return self.name



class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=1000)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
	completed = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)
	date_completed = models.DateField(null=True, blank=True)

	def __str__(self):
		return self.title


