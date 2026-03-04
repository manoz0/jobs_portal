# jobs/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'), 
    
]