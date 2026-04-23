from django.urls import path
from . import views # работает только с функциями (def)
from tasks.views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete # работает только с классами 

app_name = 'tasks'

urlpatterns = [
    path("", TaskList.as_view(), name='task-list'),
    path('<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('create/', TaskCreate.as_view(), name='task-create'),
    path('<int:pk>/update/', TaskUpdate.as_view(), name='task-update'),
    path('<int:pk>/delete/', TaskDelete.as_view(), name='task-delete'),
]
