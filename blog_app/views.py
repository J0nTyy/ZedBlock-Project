from django.shortcuts import render, redirect
from . import models
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
import django.contrib.auth
from django.contrib import messages


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
        'posts': Post.objects.all().order_by('date_posted').reverse()
    }
    return render(request, 'blog_app/home_page.html', context)


def create_new_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        new_post = models.Post(title=title, content=content, author=request.user)
        new_post.save()
        return redirect('/home')
    if request.user.is_authenticated:
        return render(request, 'blog_app/create_new_post.html')
    else:
        messages.error(request, 'KINDLY LOGIN TO ADD POSTS')
        return redirect('/login')


def edit_post(request, pk):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.get(id=pk)
        post.title = title
        post.content = content
        post.save()
        return redirect('/mypost')
    else:
        post = Post.objects.get(id=pk)
        context = {
            'post': post
        }
        return render(request, 'blog_app/edit_post.html', context)


def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('/mypost')


def my_post(request):
    if request.user.is_authenticated:
        context = {
            'posts': Post.objects.filter(author=request.user)
        }
        return render(request, 'blog_app/my_post.html', context)
    else:
        messages.error(request, 'KINDLY LOGIN TO VIEW YOUR POSTS')
        return redirect('/login')


def signout(request):
    logout(request)
    return redirect('/login')
