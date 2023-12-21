from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('login/', views.login),
    path('home/', views.home_page),
    path('newpost/', views.create_new_post, name='new-post'),
    path('mypost/', views.my_post, name='my-post'),
    path('signout/', views.signout, name='signout-btn'),
    path('edit/<int:post_id>', views.edit_post),
    path('delete/<int:post_id>', views.delete_post),
    path('read/<int:post_id>/', views.read_post, name='read_post'),
]
