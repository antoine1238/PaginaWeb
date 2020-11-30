from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views.generic.list import ListView  

""" Local."""
from .models import Post

class PostView(ListView):
    template_name = "blog/home.html"
    context_object_name = "posts"
    model = Post
    queryset = Post.objects.all()
    
    
class BlogDetailview(ListView):
    template_name = "blog/blog_1.html"
    queryset = Post.objects.all()
    context_object_name = "posts"
    model = Post
    
class BlogDetailview_2(ListView):
    template_name = "blog/blog_2.html"
    queryset = Post.objects.all()
    context_object_name = "posts"
    model = Post
    
class BlogDetailview_3(ListView):
    template_name = "blog/blog_3.html"
    queryset = Post.objects.all()
    context_object_name = "posts"
    model = Post

class BlogDetailview_4(ListView):
    template_name = "blog/blog_4.html"
    queryset = Post.objects.all()
    context_object_name = "posts"
    model = Post