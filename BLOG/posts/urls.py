from django.urls import path
from .views import PostListView, PostDetailedView, PostCreateView, PostUpdateView, PostDeleteView
# Ensure these views are defined in views.py with the exact names and inherit from Django's generic views.

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('detailed/<int:pk>/', PostDetailedView.as_view(), name='post_detail'),
    path('new/', PostCreateView.as_view(), name='post_create'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]