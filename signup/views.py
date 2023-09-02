from django.shortcuts import render
from django.http import HttpResponse

def get_signup(request):
    return HttpResponse('This is Singup page frame!', content_type='text/plain')