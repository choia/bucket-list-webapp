from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from posts.models import Post


User = get_user_model()

class ProfileDetailView(DetailView):

	queryset = User.objects.filter(is_active=True)	
	template_name = 'profiles/user.html'


	def get_context_data(self, **kwargs):		
		context = super().get_context_data(**kwargs)		
		bucket_ongoing = Post.objects.filter(completed=False, user=self.request.user).count()
		bucket_complete = Post.objects.filter(completed=True, user=self.request.user).count()
		context['bucket_ongoing'] = bucket_ongoing
		context['bucket_complete'] = bucket_complete
		return context


	def get_object(self):
		username = self.kwargs.get("username")
		if username is None:
				raise Http404
		return get_object_or_404(User, username__iexact=username, is_active=True)


