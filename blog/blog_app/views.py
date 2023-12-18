from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return render(request, 'blog_app/login.html')


def signup(request):
    return render(request, 'blog_app/signup.html')
