from django.urls import path
from .views import (
    InterviewListCreateView,
    InterviewDetailView,
)

urlpatterns = [
    path("interviews/", InterviewListCreateView.as_view()),
    path("interviews/<int:pk>/", InterviewDetailView.as_view()),
]
