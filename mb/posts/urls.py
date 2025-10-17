from django.urls import path
from .views import PostListView
from .views import DetailView


urlpatterns = [ 
       path('', PostListView.as_view(), name='post_list'), 
        path('detailed/', DetailView.as_view(), name='post_detail'),
]