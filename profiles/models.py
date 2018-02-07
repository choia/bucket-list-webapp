from django.db import models
from django.conf import settings


def user_directory_path(instance, filename):
	return 'profiles/{}/{}'.format(instance.user.username, filename)


class Profile(models.Model):
	user 			= models.OneToOneField(settings.AUTH_USER_MODEL)
	description 	= models.TextField(max_length=300, blank=True)
	date_joined 	= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True)
	image 			= models.ImageField(upload_to=user_directory_path, null=True)
	

	class Meta:
		ordering = ['user', 'date_joined']		

	def __str__(self):
		return self.user.username
