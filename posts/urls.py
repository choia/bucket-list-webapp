from django.conf.urls import url
from .views import (
	PostListView, PostCompleteListView, PostDetailView, PostCompleteDetailView, 
	PostCreate, PostEdit, PostDelete,
)


# Post URL CONF
urlpatterns = [
		url(r'^posts/$', PostListView.as_view(), name='post-home'),
		url(r'^posts/complete/$', PostCompleteListView.as_view(), name='post-complete'),	
		url(r'^posts/(?P<pk>\d+)$', PostDetailView.as_view(), name='post-detail'),
		url(r'^posts/complete/(?P<pk>\d+)$', PostCompleteDetailView.as_view(), name='post-detail-complete'),
		url(r'^posts/create/$', PostCreate.as_view(), name='post-create'),
		url(r'^posts/(?P<pk>\d+)/edit/$', PostEdit.as_view(), name='post-edit'),
		url(r'^posts/(?P<pk>\d+)/delete/$', PostDelete.as_view(), name='post-delete'),
]