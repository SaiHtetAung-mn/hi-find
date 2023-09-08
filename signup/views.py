from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .forms import CustomSignupForm
from .models import lostUsers
from django.contrib import messages

def get_signup(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            # Create a Users instance and save it
            user_profile = lostUsers(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=make_password(form.cleaned_data['password']),  # Hash the password
                gender=form.cleaned_data['gender']
            )
            
            user_profile.save()
            messages.add_message(request, messages.SUCCESS, 'Registration successfully complete')
            #Redierct to lost post overall page if successful
            return redirect('Lost Post Overall') 
    else:
        form = CustomSignupForm()
    return render(request, 'signup.html', {'form': form})