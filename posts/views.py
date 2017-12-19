from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post
from .forms import PostForm



class PostListView(ListView):
	model = Post
	def get_queryset(self):
		return Post.objects.filter(completed=False)

	template_name = 'post_home.html'


class PostCompleteListView(ListView):
	model = Post
	def get_queryset(self):
		return Post.objects.filter(completed=True)

	template_name = 'post_complete.html'


class PostDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'


class PostCompleteDetailView(UpdateView):
	model = Post
	fields = ['title', 'description', 'anecdote', 'category', 'completed']	
	template_name = 'post_edit.html'


class PostCreate(CreateView):
	form_class = PostForm
	template_name = 'post_create.html'
	success_url = reverse_lazy('posts:post-home')

	def form_valid(self, form):
		form.instance.created_by = self.request.user
		return super(PostCreate, self).form_valid(form)


class PostEdit(UpdateView):
	model = Post
	template_name = 'post_edit.html'
	fields = ['title', 'description', 'category']
	

class PostDelete(DeleteView):
	model = Post
	template_name = 'post_delete.html'
	success_url = reverse_lazy('posts:post-home')
