from django.shortcuts import render
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


class PostEdit(UpdateView):
	model = Post
	template_name = 'post_edit.html'


class PostDelete(DeleteView):
	model = Post
	template_name = 'post_delete.html'
