from django.forms import ModelForm
from .models import PostInstance


class PostInstanceForm(ModelForm):
	
	class Meta:
		model = PostInstance
		fields = ['plan', 'image']
