from django.db import models
from applications.models import Application

# Create your models here.


class Interview(models.Model):
    application = models.ForeignKey(
        Application, 
        on_delete=models.CASCADE,
        related_name="interviews"
    )


    scheduled_at = models.DateTimeField()
    meeting_link = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'interview for {self.application.job.title}'
    