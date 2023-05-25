from django.http import HttpResponse
from django.shortcuts import render, redirect
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import login
import pdb


def home(request):
    return render(request, 'home.html', {"name": "Akshay"})


# def login(request):
#     return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def index(request):
    return render(request, 'index.html')

def google_login_callback(request):

    # Get the social account associated with the current user
    social_account = SocialAccount.objects.get(provider='google', user=request.user)
    print(social_account)

    # Log in the user using Django's authentication system
    
    login(request, social_account.user.email, social_account.user.password)

    # Redirect the user to the desired page after successful login
    return redirect('index')