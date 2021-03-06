from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.http import Http404
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
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
		context['user_profile'] = user_profile

		bucket_ongoing = PostInstance.objects.filter(completed=False, owner__user=self.request.user)
		bucket_complete = PostInstance.objects.filter(completed=True, owner__user=self.request.user)
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
	success_url = reverse_lazy('posts:post-home')

	def get_context_data(self, *args, **kwargs):
		post = get_object_or_404(Post, pk=self.kwargs['pk'])
		context = super().get_context_data(*args, **kwargs)
		context['post'] = post
		context['title'] = 'Create a plan for your Goal!'
		context['date'] = 'Pick a target date for completion'

		return context


	def form_valid(self, form):
		instance = form.save(commit=False)		
		post_id = Post.objects.get(pk=self.kwargs['pk'])
		user = Profile.objects.get(user=self.request.user)
		
		instance.owner = user
		instance.user_post = post_id		
		return super(PostAddView, self).form_valid(form)



class PostUpdateView(LoginRequiredMixin, UpdateView):
	model = PostInstance
	template_name = 'profiles/forms.html'
	success_url = reverse_lazy('posts:post-home')
	fields = ['plan', 'image']


	def get_context_data(self, *args, **kwargs):
		post = PostInstance.objects.filter(id=self.kwargs['pk']).first
		context = super().get_context_data(*args, **kwargs)		
		context['post'] = post	
		context['title'] = 'Update your goal!'
		context['date'] = 'Pick a target date for completion'

		return context



class PostCompleteView(LoginRequiredMixin, UpdateView):
	model = PostInstance
	template_name = 'profiles/forms.html'
	success_url = reverse_lazy('profiles:profile-detail')
	fields = ['complete_story', 'completed', 'image']


	def get_context_data(self, *args, **kwargs):
		post = PostInstance.objects.filter(id=self.kwargs['pk']).first
		context = super().get_context_data(*args, **kwargs)		
		context['post'] = post	
		context['title'] = 'Achieved your goal!'
		
		return context


	def form_valid(self, form):	
		instance = form.save(commit=False)
		qs = PostInstance.objects.filter(pk=self.kwargs['pk'], owner__user=self.request.user, completed=False)
		qs.update(completed=True)		
		qs.update(date_completed=datetime.now())

		return super(PostCompleteView, self).form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
	pass