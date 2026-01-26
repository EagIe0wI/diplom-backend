from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from .models import User, Task, Tag, Event
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.

# path('', views.index, name='index'),
def index(request):
    context = {
        'title': 'Главная',
        'message': 'Это Главная',
    }
    return render(request, 'index.html', context)

# path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...

# path("logout/", views.logout_view, name='logout'),
def logout_view(request):
    logout(request)
    return redirect('index')
    # Redirect to a success page.

# path('tasks/', views.task_list, name='task-list'),
def task_list(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
        'title': 'Задачи',
        'message': 'Здесь Задачи'
    }
    return render(request, "task-list.html", context)

# path('tags/', views.tag_list, name='tag-list'),
def tag_list(request):
    tags = Tag.objects.all()
    context = {
        'tags': tags,
        'title': 'Тэги',
        'message': 'Здесь Тэги'
    }
    return render(request, "tag-list.html", context)

# path('events/', views.event_list, name='event-list'),
def event_list(request):
    events = Event.objects.all()
    context = {
        'events': events,
        'title': 'События',
        'message': 'Здесь События'
    }
    return render(request, "event-list.html", context)

# path('calendar/', views.calendar, name='calendar'),
def calendar(request):
    context = {
        'title': 'Каллендарь',
        'message': 'Это Календарь',
    }
    return render(request, 'calendar.html', context)

# # path("/add/", TaskCreateView.as_view(), name="task-add"),
# class TaskCreateView(CreateView):
#     template_name = "Task-form.html"
#     model = Task
#     fields = "__all__"
#     success_url = reverse_lazy("Tasks-list")

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context["title"] = "Создание товара"
#         context["message"] = "Создайте товар"
#         context["button"] = "Добавить"
#         return context

# # path("tasks/task/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
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

# # path("tasks/task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
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