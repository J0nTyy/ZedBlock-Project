from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def login(request):
    return render(request, 'blog_app/login.html')


def signup(request):
    return render(request, 'blog_app/signup.html')


def home_page(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog_app/home_page.html', context)
