from django.urls import path
from . import views

urlpatterns = [
    path('create_post/', views.createPost, name='Create Post'),
    path('lost_post_overall/', views.postOverall, name='Lost Post Overall'),
    path('lost_post_detail/', views.postDetail, name='Lost Post Detail'),
    path('user_posts/', views.userPosts, name='User Posts'),
    
]