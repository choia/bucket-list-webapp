from django.conf.urls import url
from . import views

urlpatterns = [
		url(r'^$', views.post_home, name='post_home'),	
]