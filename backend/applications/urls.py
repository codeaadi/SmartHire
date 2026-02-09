from django.urls import path
from .views import (
    ApplyJobView,
    RecruiterApplicationsView,
    UpdateApplicationStatusView,
)

urlpatterns = [
    path("", ApplyJobView.as_view()),
    path("recruiter/", RecruiterApplicationsView.as_view()),
    path("<int:pk>/status/", UpdateApplicationStatusView.as_view()),
]
