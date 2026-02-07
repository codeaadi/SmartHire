from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from .models import CompanyProfile, CandidateProfile
from .serializers import CompanyProfileSerializer, CandidateProfileSerializer


class RegisterView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message:User created successfully'},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors,status=404)
    
    
    
class candidateProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    
    
    def get(self,request):
        profile, _ = CandidateProfile.objects.get_or_create(user = request.user) 
        serializer = CandidateProfileSerializer(profile)
        
        return Response(serializer.data)
  
  
    def post(self,request):
        profile,_ = CandidateProfile.objects.get_or_create(user=request.user)
        serializer =CandidateProfileSerializer(profile,data=request.data,partial =True)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
    
    
class companyProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        profile,_=CompanyProfile.objects.get_or_create(user=request.user)
        serializer = CompanyProfileSerializer(profile)
        return Response(serializer.data)    
    
    def post(self,request):
        profile,_ =CandidateProfile.objects.get_or_create(user=request.user)
        serializer = CandidateProfileSerializer(profile,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
        
        