from django.urls import path
from . import views # работает только с функциями (def)
from tasks.views import TaskList # работает только с классами 

app_name = 'tasks'

urlpatterns = [
    path("", TaskList.as_view(), name='task_list'),
    path('create/', views.task_create, name='task_create'),
    path('<int:pk>/update/', views.task_update, name='task_update'),
    path('<int:pk>/delete/', views.task_delete, name='task_delete'),
]