from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import TaskCreateView, TaskUpdateView, TaskDeleteView

# Home, Login, User, Task, Tag, Event
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('tasks/', views.task_list, name='task-list'),
    path('tags/', views.tag_list, name='tag-list'),
    path('events/', views.event_list, name='event-list'),
    path('calendar/', views.calendar, name='calendar'),
    # path('task/add/', TaskCreateView.as_view(), name='task-add'),
    # path('task/task/<int:pk>/', TaskUpdateView.as_view(), name='task-update'),
    # path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]
