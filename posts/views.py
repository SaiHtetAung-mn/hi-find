from django.shortcuts import render
from django.http import HttpResponse

def posts(request):
    return HttpResponse('This is Posts page frame!', content_type='text/plain')