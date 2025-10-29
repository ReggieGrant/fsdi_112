from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Status
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



# Create your views here.
class PostListView(ListView):
    # model = Post
    template_name = 'posts/list.html'
    context_object_name = 'posts'
    published_status = Status.objects.get(name='published') # Get the 'published' status object
    queryset = Post.objects.filter(status=published_status).order_by("created_on").reverse()  # Filter posts with 'published' status and order by creation date descending
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        numbers = [1, 2, 3, 4, 5]
        flag = True
        context['numbers'] = numbers
        context['flag'] = flag
        print(context)
        return context



   

class PostDetailedView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/new.html'
    fields = ['title', 'subtitle', 'body', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'posts/edit.html'
    fields = ['title', 'subtitle', 'body', 'status']

    def test_func(self):
        post = self.get_object() # Get the post being updated
        if self.request.user.is_authenticated: # Check if user is authenticated
            return self.request.user == post.author # Allow update only if the user is the author




class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object() # Get the post being deleted
        if self.request.user.is_authenticated: # Check if user is authenticated
            return self.request.user == post.author # Allow delete only if the user is the author
        


class DraftPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/drafts.html'
    context_object_name = 'draft_posts'
    
      
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft_status = Status.objects.get(name='draft') # Get the 'draft' status object
        context['draft_posts'] = Post.objects.filter(status=draft_status).filter(author=self.request.user).order_by("created_on").reverse()
        return context
    

class ArchivedPostListView(LoginRequiredMixin, ListView):
    # model = Post
    template_name = 'posts/archived.html'
    archived_status_status = Status.objects.get(name='archived') # Get the 'draft' status object
    context_object_name = 'archived_posts'
    archived_status = Status.objects.get(name='archived') # Get the 'archived' status object
    queryset = Post.objects.all().filter(status=archived_status_status).order_by("created_on").reverse()   # Filter posts with 'archived' status and order by creation date descending
    def test_func(self):
        if self.request.user.is_authenticated: # Check if user is authenticated
            return self.request.user.is_staff # Allow access only if the user is staff/admin
    
