from django.shortcuts import render
from django.views.generic import ListView ,DetailView
from . models import Blog

# Create your views here.
class BlogView(ListView):
    model= Blog
    template_name='blog/blog.html'

class BlogDetail(DetailView):
    model= Blog
    template_name='blog/blog_detail.html'  

