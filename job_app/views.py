from .models import Job
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
# from .models import CustomUser

def home(request):
    jobs = Job.objects.all()

    role = request.GET.get("role")
    location = request.GET.get("location")

    if role:
        jobs = jobs.filter(role__icontains=role)

    if location:
        jobs = jobs.filter(location__icontains=location)

    return render(request, "index.html", {"jobs": jobs})



def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password != password2:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Account created successfully! Please log in.")
            return redirect("login")

    return render(request, "register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")  # Redirect to your homepage
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")