from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView
from posts.models import Post
from .models import Profile, PostInstance
from .forms import PostInstanceForm


User = get_user_model()

class ProfileDetailView(LoginRequiredMixin, DetailView):

	queryset = User.objects.filter(is_active=True)	
	template_name = 'profiles/user.html'


	def get_context_data(self, **kwargs):		
		context = super().get_context_data(**kwargs)		
		user_profile = Profile.objects.filter(user=self.request.user)
		bucket_ongoing = Profile.objects.filter(user=self.request.user).count()
		bucket_complete = Profile.objects.filter(user=self.request.user).count()
		context['user_profile'] = user_profile
		context['bucket_ongoing'] = bucket_ongoing
		context['bucket_complete'] = bucket_complete

		return context


	def get_object(self):
		username = self.kwargs.get("username")
		
		if username is None:
				raise Http404
		if username == self.request.user.username:
			return get_object_or_404(User, username__iexact=username, is_active=True)
		else: raise Http404



class PostAddView(LoginRequiredMixin, CreateView):
	

	template_name = 'profiles/forms.html'
	form_class = PostInstanceForm


	def get_context_data(self, *args, **kwargs):
		post_id = get_object_or_404(Post, pk=self.kwargs['pk'])
		context = super().get_context_data(*args, **kwargs)
		context['post_id'] = post_id
		context['title'] = 'Create a Goal!'


		return context


	# def get_queryset(self):
	# 	self.post_id = get_object_or_404(Post, pk=self.kwargs['pk'])
	# 	return Post.objects.filter(pk=self.post_id)