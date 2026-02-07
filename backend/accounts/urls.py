from django.urls import path
from .views import RegisterView, companyProfileView,candidateProfileView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('login/',TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('candidate/profile',candidateProfileView.as_view()),
    path('company/profile',companyProfileView.as_view()),
]
