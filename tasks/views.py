from .models import Task
from django.http import JsonResponse
import json
from django.views import View

# Create your views here.

class TaskList(View):
    def get(request):
        username = json.loads(request.body)
        tasks = Task.objects.all(username)
        # tasks = request.POST[username]
        print(tasks)
        
        return JsonResponse({"status": "success at task_list"})
