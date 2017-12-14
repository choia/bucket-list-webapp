from django.conf.urls import url
from . import views


# Post URL CONF
urlpatterns = [
		url(r'^posts/$', views.PostListView.as_view(), name='post-home'),	
		url(r'^posts/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post-detail'),
		url(r'^posts/create/$', views.PostCreate.as_view(), name='post-create'),
		url(r'^posts/(?P<pk>\d+)/edit/$', views.PostEdit.as_view(), name='post-edit'),
		url(r'^posts/(?P<pk>\d+)/delete/$', views.PostDelete.as_view(), name='post-delete'),
]