from django.urls import path, include
from cards.views import CardListView, CardDetailView, CardCreateView, CardUpdateView, CardDeleteView
from rest_framework.routers import DefaultRouter

app_name = 'cards'

router = DefaultRouter()
router.register(r'cards', CardListView)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', CardDetailView.as_view(), name='card-detail'),
    path('create/', CardCreateView.as_view(), name='card-create'),
    path('<int:pk>/update/', CardUpdateView.as_view(), name='card-update'),
    path('<int:pk>/delete/', CardDeleteView.as_view(), name='card-delete'),
]
