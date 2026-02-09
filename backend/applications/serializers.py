from rest_framework import serializers
from .models import Application


class ApplicationSerialiser(serializers.ModelSerializer):
    candidate_email = serializers.ReadOnlyField(source='candidate.email')
    job_title = serializers.ReadOnlyField(source ='job.title')
    
    
    class Meta:
        model = Application
        fields = '__all__'
        read_only_field = ['candidate','status']