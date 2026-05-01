from .models import Task
from django.http import JsonResponse
import json
from django.views import View

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
class TaskList(View):
    def task_list(request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

# class TaskList(View):
#     def get(self, request):
#         username = json.loads(request.body)
#         tasks = Task.objects.all(username)
#         # tasks = request.POST[username]
#         print(tasks)
        
#         return JsonResponse({"status": "response from task-list"})

class TaskDetail(View):
    def get(self, request):
        return JsonResponse({"status": "response from task-detail"})

class TaskCreate(View):
    # здесь нужна form
    def get(self, request):
        return JsonResponse({"status": "response from task-create"})

class TaskUpdate(View):
    # здесь нужна form
    def get(self, request):
        return JsonResponse({"status": "response from task-update"})

class TaskDelete(View):
    # здесь нужна form
    def get(self, request):
        return JsonResponse({"status": "response from task-delete"})
