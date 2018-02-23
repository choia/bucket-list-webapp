from django.conf.urls import url
from .views import (
	ProfileDetailView, PostAddView, PostUpdateView,
)


# PROFILES URL CONF
urlpatterns = [
	url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='profile-detail'),
	url(r'^(?P<username>[\w-]+)/(?P<pk>\d+)/add/$', PostAddView.as_view(), name='post-add'),
	url(r'^(?P<username>[\w-]+)/(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name='post-update'),
]