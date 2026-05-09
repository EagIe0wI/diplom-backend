from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from tags.views import TagListView, TagDetailView, TagCreateView, TagUpdateView, TagDeleteView

app_name = 'tags'

router = DefaultRouter()
router.register(r'tags', TagListView)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', TagDetailView.as_view(), name='tag-detail'),
    path('create/', TagCreateView.as_view(), name='tag-create'),
    path('<int:pk>/update/', TagUpdateView.as_view(), name='tag-update'),
    path('<int:pk>/delete/', TagDeleteView.as_view(), name='tag-delete'),
]
