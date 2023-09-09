from django.shortcuts import render
from django.http import HttpResponse
import logging
logger = logging.getLogger('hi_find')

def createPost(request):
    return render(request,'create_post.html')

def postOverall(request):
    return render(request,'lostpost_overall.html')

def postDetail(request):
    return render(request,'lostpost_detail.html')

def userPosts(request):
    return render(request,'user_posts.html')