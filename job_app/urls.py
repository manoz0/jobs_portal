# jobs/urls.py
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('addjob/', views.addjob, name='addjob'),
    path('jobs/delete/<int:id>/', views.delete_job, name='delete_job'),
    path('jobs/edit/<int:id>/', views.edit_job, name='edit_job'),
    
]