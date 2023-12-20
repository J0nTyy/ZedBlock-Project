from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup),
    path('login/', views.login),
    path('home/', views.home_page),
    path('newpost/', views.create_new_post, name='new-post'),
    path('mypost/', views.my_post, name='my-post'),
    path('signout/', views.signout, name='signout-btn'),
    path('edit/', views.edit_post),
]
