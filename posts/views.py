from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from .models import Post, Category
from .forms import PostForm



class PostListView(LoginRequiredMixin, ListView):
	model = Post	
	context_object_name = 'posts'
	template_name = 'post_home.html'

	def get_context_data(self, **kwargs):
		context = super(PostListView, self).get_context_data(**kwargs)
		context['categories'] = Category.objects.filter(
			Q(name__iexact='Travel') |
 			Q(name__iexact='Adventure') |
 			Q(name__iexact='Learn New Things')).distinct()

		context['posts'] = Post.objects.all()
		context['travels'] = Post.objects.filter(category__name__iexact='Travel')[:6]
		context['adventures'] = Post.objects.filter(category__name__iexact='Adventure')[:6]
		context['lnts'] = Post.objects.filter(category__name__iexact='Learn New Things')[:6]

		return context

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
