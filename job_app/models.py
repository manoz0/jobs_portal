from django.db import models
from django.contrib.auth.models import AbstractUser

class Job(models.Model):
    ROLE_CHOICES = [
        ('Frontend Developer', 'Frontend Developer'),
        ('Backend Developer', 'Backend Developer'),
        ('Data Analyst', 'Data Analyst'),
        ('UI/UX Designer', 'UI/UX Designer'),
        ('Python Developer', 'Python Developer'),
    ]

    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    description = models.TextField()
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
