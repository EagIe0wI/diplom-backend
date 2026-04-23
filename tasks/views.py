from .models import Task
from django.http import JsonResponse
import json
from django.views import View

class TaskList(View):
    def get(request):
        username = json.loads(request.body)
        tasks = Task.objects.all(username)
        # tasks = request.POST[username]
        print(tasks)
        
        return JsonResponse({"status": "response from task-list"})

class TaskDetail(View):
    def get(request):
        return JsonResponse({"status": "response from task-detail"})

class TaskCreate(View):
    # здесь нужна form
    def get(request):
        return JsonResponse({"status": "response from task-create"})

class TaskUpdate(View):
    # здесь нужна form
    def get(request):
        return JsonResponse({"status": "response from task-update"})

class TaskDelete(View):
    # здесь нужна form
    def get(request):
        return JsonResponse({"status": "response from task-delete"})
