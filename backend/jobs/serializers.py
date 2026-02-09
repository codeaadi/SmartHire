from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):
    company_email= serializers.ReadOnlyField(source='company.email')
    
    
    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ['company']
        