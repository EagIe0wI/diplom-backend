from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import TaskCreateView#, TaskUpdateView, TaskDeleteView

# Home, Login, User, Task, Tag, Event
urlpatterns = [
    path('', views.index_view),
    path('register/', views.register_view),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('tasks/', views.task_list),
    # path('tasks/<int:pk>/', views.task_detail),
    # path('tasks/addTask/', views.task_add),
    path('tasks/addTask/', TaskCreateView.as_view()),
    # path('tasks/<int:pk>/updateTask/', TaskUpdateView.as_view()),
    # path('tasks/<int:pk>/deleteTask/', TaskDeleteView.as_view()),
    # path('tags/', views.tag_list),
    # path('events/', views.event_list),
    # path('calendar/', views.calendar),
]
