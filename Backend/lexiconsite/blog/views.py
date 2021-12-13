from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import render
from django.http import HttpResponse

class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/blog_list.html'


class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/blog_detail.html'


