from django.db import models
from django.contrib.auth.models import AbstractUser


class Job(models.Model):
    DOMAIN_CHOICES = [
        ('IT', 'IT'),
        ('Finance', 'Finance'),
        ('Marketing', 'Marketing'),
        ('Healthcare', 'Healthcare'),
        ('Engineering', 'Engineering'),
    ]

    JOB_TYPE = [
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Remote', 'Remote'),
        ('Internship', 'Internship'),
    ]

    EXPERIENCE = [
        ('Fresher', 'Fresher'),
        ('1-3 Years', '1-3 Years'),
        ('3-5 Years', '3-5 Years'),
        ('5+ Years', '5+ Years'),
    ]

    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    domain = models.CharField(max_length=100, choices=DOMAIN_CHOICES, default="IT")
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE,default="Full-Time")
    experience = models.CharField(max_length=50, choices=EXPERIENCE,default="Fresher")
    salary = models.CharField(max_length=100,default="20000")
    description = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title