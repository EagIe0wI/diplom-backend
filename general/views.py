from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from .models import User, Task, Tag, Event
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

# path('', views.index, name='index'),
def index(request):
    context = {
        'title': 'Главная',
        'message': 'Это Главная',
    }
    return render(request, 'index.html', context)

# path('register/', views.register_view, name='register'),
@csrf_exempt
def register_view(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    user = User.objects.create_user(username=username, password=password)
    user.save()
    redirect(task_list)
    return JsonResponse({"status": "success login"})

# path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
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

# path("logout/", views.logout_view, name='logout'),
def logout_view(request):
    logout(request)
    return redirect('index')
    # Redirect to a success page.

# path('tasks/', views.task_list, name='task-list'),
def task_list(request):
    username = json.loads(request.body)
    tasks = Task.objects.all(username)
    # tasks = request.POST[username]
    print(tasks)
    
    return JsonResponse({"status": "success at task_list"})

# path('tasks/task/', views.task, name='task'),

# path('tags/', views.tag_list, name='tag-list'),
# path('events/', views.event_list, name='event-list'),
# path('calendar/', views.calendar, name='calendar'),

# path('tasks/addTask/', TaskCreateView.as_view(), name='task-add'),
# class TaskCreateView(CreateView):
#     template_name = "task-form.html"
#     model = Task
#     fields = "__all__"
#     success_url = reverse_lazy("task-list")

def task_add(request):
    taskData = json.loads(request.body)
    print(taskData)
    # tasks = request.POST[username]
        
    return JsonResponse({"status": "success", "task data": taskData})

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     return context

# # path('tasks/<int:pk>/updateTask/', TaskUpdateView.as_view(), name='task-update'),
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

# # path('tasks/<int:pk>/deleteTask/', TaskDeleteView.as_view(), name='task-delete'),
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