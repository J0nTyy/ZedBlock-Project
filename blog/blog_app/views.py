from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
import django.contrib.auth


def login(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('upassword')
        user = authenticate(request, username=name, password=password)
        if user is not None:
            django.contrib.auth.login(request, user)
            return redirect('/home')
        else:
            redirect('/login')
    return render(request, 'blog_app/login.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')
        new_user = User.objects.create_user(username=name, email=email, password=password)
        new_user.save()
        return redirect('/login')
    return render(request, 'blog_app/signup.html')


def home_page(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog_app/home_page.html', context)
