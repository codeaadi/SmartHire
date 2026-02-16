from rest_framework.views import APIView
from rest_framework.response import Response
from jobs.models import Job
from applications.models import Application
from interviews.models import Interview



class RecruiterDashboardView(APIView):
    def get(self,request):
        user = request.user
        
        
        jobs = Job.objects.filter(created_by=user)
        applications = Application.objects.filter(job_in=jobs)
        
        
        data = {
            'jobs_posted': jobs.count(),
            'applicatoins':applications.count(),
            'shortlisted':applications.filter(status='shortlisted').count(),
            'interviews':Interview.objects.filter(
                applications_in=applications
            ).count(),
            'hired':applications.filter(status='hired').count(),
        } 
        
        return Response(data)