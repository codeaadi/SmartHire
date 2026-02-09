from rest_framework import permissions, generics
from .models import Job
from .serializers import JobSerializer


class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all().order_by('-created_at')
    serializer_class = JobSerializer
    permission_classes =[permissions.IsAuthenticatedOrReadOnly]
    
    
    def perform_create(self, serializer):
        serializer.save(company=self.request.user)


class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]