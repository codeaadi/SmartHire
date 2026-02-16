from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Interview
from .serializers import InterviewSerializer
from django.shortcuts import get_object_or_404


class InterviewListCreateView(APIView):
    def get(self, request):
        interviews = Interview.objects.all()
        serializer = InterviewSerializer(interviews, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InterviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class InterviewDetailView(APIView):
    def get(self, request, pk):
        interview = get_object_or_404(Interview, pk=pk)
        serializer = InterviewSerializer(interview)
        return Response(serializer.data)

    def put(self, request, pk):
        interview = get_object_or_404(Interview, pk=pk)
        serializer = InterviewSerializer(interview, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        interview = get_object_or_404(Interview, pk=pk)
        interview.delete()
        return Response(status=204)
