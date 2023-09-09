from django.urls import path
from . import views

urlpatterns = [
    path('create_post/', views.createPost, name='Create Post'),
    path('lost_post_overall/', views.postOverall, name='Lost Post Overall'),
    path('lost_post_detail/<int:post_id>/', views.postDetail, name='Lost Post Detail'),  # URL for post detail
    path('user_posts/', views.userPosts, name='User Posts'),
    
]