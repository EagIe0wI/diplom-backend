from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from .models import CustomUser, Task, Tag, Event
from django.views.generic.edit import CreateView#, DeleteView, UpdateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

def index_view(request):
    context = {
        'title': 'Главная',
        'message': 'Это Главная',
    }
    return render(request, 'index.html', context)

@csrf_exempt
def register_view(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    user = CustomUser.objects.create_user(username=username, password=password)
    user.save()
    redirect(task_list)
    return JsonResponse({"status": "success registration"})

@csrf_exempt
def login_view(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        redirect(task_list)
        return JsonResponse({"status": "success login"})
    else:
        # Return an 'invalid login' error message.
        return JsonResponse({"status": "invalid login"})

def logout_view(request):
    logout(request)
    return redirect('index')
    # Redirect to a success page.

def task_list(request):
    username = json.loads(request.body)
    tasks = Task.objects.all(username)
    # tasks = request.POST[username]
    print(tasks)
    
    return JsonResponse({"status": "success at task_list"})

@csrf_exempt
class TaskCreateView(CreateView):
    template_name = "task-form.html"
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task-list")

# @csrf_exempt
# def task_add(request):
#     taskData = json.loads(request.body)
#     print(taskData)
#     # tasks = request.POST[username]
        
#     return JsonResponse({"status": "success", "task data": taskData})

# class TaskUpdateView(UpdateView):
#     template_name = "Task-form.html"
#     model = Task
#     fields = "__all__"
#     success_url = reverse_lazy("Tasks-list")

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context["title"] = "Редактирование товара"
#         context["message"] = "Отредактируйте товар"
#         context["button"] = "Подтвердить"
#         return context

# class TaskDeleteView(DeleteView):
#     template_name = "Task-delete.html"
#     model = Task
#     success_url = reverse_lazy("Tasks-list")

#     def delete(request, Task_id):
#         Task = get_object_or_404(Task, pk=Task_id)
#         if request.method == "POST":
#             try:
#                 Task.delete()
#             except ProtectedError:
#                 text_message = "Продукт удалить нельзя, он содержится в составе заказа!"
#                 return render(request, "Task/delete.html", {"Task": Task, "text_message": text_message})
#             return redirect('list_Tasks')
#         return render(request, "Task/delete.html", {"Task": Task})