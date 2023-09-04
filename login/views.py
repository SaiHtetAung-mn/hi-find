from django.shortcuts import render
from django.http import HttpResponse



def get_login(request):
    return render(request, 'login.html')