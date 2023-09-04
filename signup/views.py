from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .forms import CustomSignupForm
from .models import Users

def get_signup(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            # Create a UserProfile instance and save it
            user_profile = Users(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=make_password(form.cleaned_data['password']),  # Hash the password
                gender=form.cleaned_data['gender']
            )
            user_profile.save()
            return redirect('index')  # Replace 'index' with your desired success page
    else:
        form = CustomSignupForm()
    return render(request, 'signup/signup.html', {'form': form})