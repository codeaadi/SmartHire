from rest_framework import generics, permissions
from .models import Application
from .serializers import ApplicationSerializer


class ApplyJobView(generics.ListCreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Application.objects.filter(candidate=self.request.user)

    def perform_create(self, serializer):
        serializer.save(candidate=self.request.user)


class RecruiterApplicationsView(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Application.objects.filter(job__company=self.request.user)


class UpdateApplicationStatusView(generics.UpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

