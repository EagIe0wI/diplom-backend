from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from categories.views import CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView

app_name = 'categories'

router = DefaultRouter()
router.register(r'categories', CategoryListView)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('create/', CategoryCreateView.as_view(), name='category-create'),
    path('<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
]
