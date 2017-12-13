from django.conf.urls import url
from . import views


urlpatterns = [
		url(r'^posts/$', views.PostListView.as_view(), name='post-home'),	
]