from django.urls import path, include
from tasks.views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView
from rest_framework.routers import DefaultRouter

app_name = 'tasks'

router = DefaultRouter()
router.register(r'tasks', TaskListView)

urlpatterns = [
    path('', include(router.urls)),
    # path('list/', TaskList.as_view(), name='task-list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
]
