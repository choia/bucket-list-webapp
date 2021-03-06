from django.conf.urls import url
from .views import (
	ProfileDetailView, PostAddView, PostUpdateView, PostCompleteView, PostDeleteView,
)


# PROFILES URL CONF
urlpatterns = [
	url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='profile-detail'),
	url(r'^(?P<username>[\w-]+)/(?P<pk>\d+)/add/$', PostAddView.as_view(), name='post-add'),
	url(r'^(?P<username>[\w-]+)/(?P<pk>\d+)/update/$', PostUpdateView.as_view(), name='post-update'),
	url(r'^(?P<username>[\w-]+)/(?P<pk>\d+)/complete/$', PostCompleteView.as_view(), name='post-complete'),
	url(r'^(?P<username>[\w-]+)/(?P<pk>\d+)/delete/$', PostDeleteView.as_view(), name='post-delete'),
]