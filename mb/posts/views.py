from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse_lazy

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


class PostCreateView(CreateView):
    """View to create a new blog post."""
    
    template_name = 'posts/new.html' # specify your template name
    model = Post # specify the model to use
    fields = ['title', 'subtitle','body'] # fields to include in the form

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        print(form)
        print(User.objects.all())
        form.instance.author = User.objects.filter(is_superuser=True).first() # set the author to the first user
        return super().form_valid(form)
    


class PostUpdateView(UpdateView):
    """View to update an existing blog post."""
    
    template_name = 'posts/edit.html' # specify your template name
    model = Post # specify the model to use
    fields = ['title', 'subtitle','body'] # fields to include in the form
    


class PostDeleteView(DeleteView):
    """View to delete a blog post."""
    
    template_name = 'posts/delete.html' # specify your template name
    model = Post # specify the model to use
    success_url = reverse_lazy('post_list') # URL to redirect to after deletion
    

    
    
    

   