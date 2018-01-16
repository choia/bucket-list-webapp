from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from django.db.models import Q


class Category(models.Model):
	name = models.CharField(max_length=100, help_text="Category for the Bucketlist (e.g. Travel, Milestone, Skills")

	def __str__(self):
		return self.name


class Post(models.Model):
	user 			= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	title 			= models.CharField(max_length=50)
	description 	= models.TextField(max_length=1000)
	anecdote		= models.TextField(max_length=2000, null=True, blank=True)
	category 		= models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
	completed 		= models.BooleanField(default=False)
	date_created 	= models.DateTimeField(auto_now_add=True)
	date_updated 	= models.DateTimeField(auto_now=True)
	date_completed  = models.DateTimeField(auto_now=True, null=True, blank=True)
	image		 	= models.ImageField(upload_to='posts/%Y/%m/%d', null=True)


	class Meta:
		ordering = ['-pk']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('posts:post-detail', kwargs={'pk': self.pk})

	# def category_is_blank(self):
	# 	if self.category:
	# 		return self.category
	# 	else: return ''

		