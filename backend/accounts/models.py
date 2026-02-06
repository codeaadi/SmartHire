from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('candidate','Candidate'),
        ('recruiter','Recruiter'),
        ('admin','Admin')
    )
    email =models.EmailField(unique=True)
    role = models.CharField(max_length=50,choices=ROLE_CHOICES)
    
    
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.email