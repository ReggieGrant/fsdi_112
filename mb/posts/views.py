from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
# class based views and function based views


class PostListView(ListView):
    """View to list all blog posts."""
    
    template_name = 'posts/list.html' # specify your template name
    model = Post # specify the model to use
    context_object_name = 'posts' # name of the context variable in the template
    
class PostDetailView(DetailView):
    """View to display a single blog post."""
    
    template_name = 'posts/detail.html' # specify your template name
    model = Post # specify the model to use
    context_object_name = 'detailed' # name of the context variable in the template
    

   