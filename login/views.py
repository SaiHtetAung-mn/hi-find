from django.shortcuts import render
from django.http import HttpResponse

def get_login(request):
    return HttpResponse('This is login page frame!', content_type='text/plain')