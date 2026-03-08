from .models import Job
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# from .models import CustomUser

def home(request):
    jobs = Job.objects.all()

    domain = request.GET.get('domain')
    role = request.GET.get("role")
    location = request.GET.get("location")

    if domain:
        jobs = jobs.filter(domain=domain)

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
        if user :
            login(request, user)
            if user.is_superuser:
                return redirect('dashboard')
            else:
                return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")



#dashboard

@login_required
def dashboard(request):
    jobs=Job.objects.all()
    return render(request,"dashboard.html",{'jobs':jobs})


@login_required
def addjob(request):
    if request.method == "POST":
        title = request.POST.get('title')
        company = request.POST.get('company')
        location = request.POST.get('location')
        salary = request.POST.get('salary')
        #description = request.POST.get('description')

        Job.objects.create(
            title=title,
            company=company,
            location=location,
            salary=salary,
            #description=description
        )
        return redirect('dashboard')

    return render(request, 'addjob.html')


@login_required
def edit_job(request, id):
    job = get_object_or_404(Job, id=id)

    if request.method == "POST":
        job.title = request.POST.get('title')
        job.company = request.POST.get('company')
        job.location = request.POST.get('location')
        job.salary = request.POST.get('salary')
        job.description = request.POST.get('description')
        job.save()
        return redirect('dashboard')
    

    return render(request,'edit.html', {'job': job})


@login_required
def delete_job(request, id):
    job = get_object_or_404(Job, id=id)
    job.delete()
    return redirect('dashboard')