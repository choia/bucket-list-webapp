from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
# from posts.models import Post



def user_directory_path(instance, filename):
	return 'profiles/{}/{}'.format(instance.user.username, filename)

def post_directory_path(instance, filename):
	return 'profiles/{}/{}/%Y/%m/%d'.format(instance.user.username, filename)	


class Profile(models.Model):
	user 			= models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	description 	= models.TextField(max_length=300, blank=True)
	date_joined 	= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True)
	image 			= models.ImageField(upload_to=user_directory_path, null=True, blank=True)
	is_active		= models.BooleanField(default=True)


	class Meta:
		ordering = ['user', 'date_joined']		

	def __str__(self):
		return self.user.username

	def get_full_name(self):
		return self.user.first_name + self.user.last_name


class PostInstance(models.Model):
	completed 		= models.BooleanField(default=False)
	date_completed  = models.DateTimeField(auto_now=True, null=True, blank=True)
	complete_story	= models.TextField(max_length=500, blank=True)
	# post			= models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
	image 			= models.ImageField(upload_to=post_directory_path, null=True, blank=True)

	# class Meta:
	# 	ordering = ['post_instance']

	# def __str__(self):
	# 	return self.post_instance.title