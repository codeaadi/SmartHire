from django.db import models
from django.conf import settings
# Create your models here.


class Job(models.Model):
    JOB_TYPE= (
        ('full_time','Full Time'),
        ('part_time','Part Time'),
        ('internship','Internship'),
    )
    
    company = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='jobs',
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=200)
    salary = models.IntegerField(null=True,blank=True)
    job_type = models.CharField(max_length=100,choices=JOB_TYPE)
    
    created_at = models.DateTimeField(auto_now_add=True)
    