from django.urls import path
from .views import PostListView, PostDetailedView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailedView.as_view(), name='post_detail'),
]