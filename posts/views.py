from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post



class PostListView(ListView):
	model = Post
	template_name = 'post_home.html'


class PostDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'


class PostCreate(CreateView):
	model = Post
	template_name = 'post_create.html'
	fields = ['title', 'description', 'category']


class PostEdit(UpdateView):
	model = Post
	template_name = 'post_edit.html'
	fields = ['title', 'description', 'category']


class PostDelete(DeleteView):
	model = Post
	template_name = 'post_delete.html'
	success_url = reverse_lazy('post-home')