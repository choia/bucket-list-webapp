from django.conf.urls import url
from .views import (
	PostListView, PostCompleteListView, PostDetailView, PostCompleteDetailView, PostCategoryListView,
	PostCreate, PostEdit, PostDelete, LogOutView,
)


# Post URL CONF
urlpatterns = [
		url(r'^$', PostListView.as_view(), name='post-home'),
		url(r'^complete/$', PostCompleteListView.as_view(), name='post-complete'),	
		url(r'^complete/(?P<pk>\d+)$', PostCompleteDetailView.as_view(), name='post-detail-complete'),
		url(r'^(?P<pk>\d+)$', PostDetailView.as_view(), name='post-detail'),
		url(r'^create/$', PostCreate.as_view(), name='post-create'),
		url(r'^(?P<pk>\d+)/edit/$', PostEdit.as_view(), name='post-edit'),
		url(r'^(?P<pk>\d+)/delete/$', PostDelete.as_view(), name='post-delete'),
		url(r'^category/$', PostCategoryListView.as_view(), name='post-all'),
		url(r'^accounts/logout/$', LogOutView.as_view(), name='logout'),
]