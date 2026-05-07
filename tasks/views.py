from .models import Task
from django.http import JsonResponse
import json
from django.views import View
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets

class TaskList(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(View):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return JsonResponse({"status": "response from task-detail"})

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

class TaskUpdate(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request, pk):
        try:
            task = Task.objects.get(pk=pk, user=request.user)
            serializer = TaskSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        except Task.DoesNotExist:
            return Response(status=404)

class TaskDelete(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        try:
            task = Task.objects.get(pk=pk, user=request.user)
            # if task.user != request.user:
            #     return Response({"error": "No permission to delete"}, status=400)
            task.delete()
            return Response(status=204)
        except Task.DoesNotExist:
            return Response(status=404)

