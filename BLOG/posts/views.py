from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post



# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'posts/list.html'
    context_object_name = 'posts'

   

class PostDetailedView(DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'
    
