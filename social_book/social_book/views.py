from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {"name": "Akshay"})


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def index(request):
    return render(request, 'index.html')