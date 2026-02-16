from django.urls import path
from .views import RecruiterDashboardView

urlpatterns = [
    path("dashboard/recruiter/", RecruiterDashboardView.as_view()),
]
