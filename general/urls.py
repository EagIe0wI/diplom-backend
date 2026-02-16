from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
# from .views import TaskCreateView, TaskUpdateView, TaskDeleteView

# Home, Login, User, Task, Tag, Event
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('tasks/', views.task_list, name='task-list'),
    # path('tasks/<int:pk>/', views.task_detail, name='task-detail'),
    path('tasks/addTask/', views.task_add, name='task-add'),
    # path('tasks/addTask/', TaskCreateView.as_view(), name='task-add'),
    # path('tasks/<int:pk>/updateTask/', TaskUpdateView.as_view(), name='task-update'),
    # path('tasks/<int:pk>/deleteTask/', TaskDeleteView.as_view(), name='task-delete'),
    # path('tags/', views.tag_list, name='tag-list'),
    # path('events/', views.event_list, name='event-list'),
    # path('calendar/', views.calendar, name='calendar'),
]
