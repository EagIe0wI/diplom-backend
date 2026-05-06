from .models import Task
from django.http import JsonResponse
import json
from django.views import View
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets
from django.shortcuts import render, redirect
# from .forms import TaskForm

class TaskList(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(View):
    def get(self, request):
        return JsonResponse({"status": "response from task-detail"})

from rest_framework.response import Response
from rest_framework.views import APIView

class TaskCreateView(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class TaskCreate(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        if request.method == "POST":
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        
        return JsonResponse({'serialiser': serializer})

class TaskUpdate(View):
    # здесь нужна form
    def get(self, request):
        return JsonResponse({"status": "response from task-update"})

class TaskDelete(View):
    # здесь нужна form
    def get(self, request):
        return JsonResponse({"status": "response from task-delete"})
