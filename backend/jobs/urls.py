from django.urls import path
from .views import JobListCreateView, JobDetailView, RecruiterJobsView

urlpatterns = [
    path("recruiter/", RecruiterJobsView.as_view()),
    path("", JobListCreateView.as_view()),
    path("<int:pk>/", JobDetailView.as_view()),
]
