from django.shortcuts import render, redirect
from . import models
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


def create_new_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        new_post = models.Post(title=title, content=content, author=request.user)
        new_post.save()
        return redirect('/home')

    return render(request, 'blog_app/create_new_post.html')


def edit_post(request, id):
    blog = User.objects.get(id=id)
    return render(request, 'blog_app/edit_post.html')


def my_post(request):
    if request.user.is_authenticated:
        context = {
            'posts': Post.objects.filter(author=request.user)
        }
        return render(request, 'blog_app/my_post.html', context)
    else:
        return redirect('/login')


def signout(request):
    logout(request)
    return redirect('/login')
