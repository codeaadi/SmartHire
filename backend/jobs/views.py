from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer
from applications.models import Application


class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all().order_by('-created_at')
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(company=self.request.user)


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class RecruiterJobsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        jobs = Job.objects.filter(company=request.user)

        data = []
        for job in jobs:
            applicant_count = Application.objects.filter(job=job).count()

            data.append({
                "id": job.id,
                "title": job.title,
                "description": job.description,
                "created_at": job.created_at,
                "applicant_count": applicant_count
            })

        return Response(data)
