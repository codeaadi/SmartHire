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
    
    
    
    # CANDIDATE PROFILE 
    
class CandidateProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=15,blank=True)
    skills =models.TextField(blank=True)
    experience = models.IntegerField(default=0)
    resume = models.FileField(upload_to='resume/',null=True,blank=True)
    
    
    def __str__(self):
        return self.user.email   
    
    
    
    
    # COMPANY PROFILE
    
    
class CompanyProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    company_name =models.CharField(max_length=150)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=150,blank=True)
    
    
    
    def __str__(self):
        return self.company_name    
    