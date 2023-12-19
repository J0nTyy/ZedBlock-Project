from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup),
    path('login/', views.login),
    path('home/', views.home_page),
]
