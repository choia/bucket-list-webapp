from django.conf.urls import url
from .views import (
	ProfileDetailView
)


# PROFILES URL CONF
urlpatterns = [
	url(r'^(?P<username>[\w-]+)/$', ProfileDetailView.as_view(), name='profile-detail'),

]