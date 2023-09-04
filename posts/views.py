from django.shortcuts import render
from django.http import HttpResponse

def createPost(request):
    return render(request,'create_post.html')