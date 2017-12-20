from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from .models import Post
from .forms import PostForm



class PostListView(LoginRequiredMixin, ListView):
	model = Post
	context_object_name = 'posts'

	def get_queryset(self):		
		return Post.objects.filter(completed=False, user=self.request.user)

	template_name = 'post_home.html'


class PostCompleteListView(LoginRequiredMixin, ListView):
	model = Post

	def get_queryset(self):
		return Post.objects.filter(completed=True, user=self.request.user)

	template_name = 'post_complete.html'


class PostDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'


class PostCompleteDetailView(LoginRequiredMixin, UpdateView):
	model = Post
	fields = ['title', 'description', 'anecdote', 'category', 'completed']	
	template_name = 'post_edit.html'


class PostCreate(LoginRequiredMixin, CreateView):
	form_class = PostForm
	template_name = 'post_create.html'
	success_url = reverse_lazy('posts:post-home')

	def form_valid(self, form):
		# form.instance.created_by = self.request.user
		instance =  form.save(commit=False)
		instance.user = self.request.user
		return super(PostCreate, self).form_valid(form)


class PostEdit(LoginRequiredMixin, UpdateView):
	model = Post
	template_name = 'post_edit.html'
	fields = ['title', 'description', 'category']
	

class PostDelete(LoginRequiredMixin, DeleteView):
	model = Post
	template_name = 'post_delete.html'
	success_url = reverse_lazy('posts:post-home')
