from django.urls import path, include
from tasks.views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView
from rest_framework.routers import DefaultRouter

app_name = 'tasks'

router = DefaultRouter()
router.register(r'tasks', TaskListView, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]
