from django.urls import path
from .views import PostListView
from .views import PostDetailView
from .views import PostCreateView
from .views import PostUpdateView
from .views import PostDeleteView


urlpatterns = [ 
        path('', PostListView.as_view(), name='post_list'), 
        path('detailed/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
        path('new/', PostCreateView.as_view(), name='post_new'),
        path('edit/<int:pk>/', PostUpdateView.as_view(), name='post_edit'),
        path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]