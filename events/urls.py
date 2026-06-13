from django.urls import path, include
from events.views import EventViewSet, EventCreateView, EventUpdateView, EventDeleteView
from rest_framework.routers import DefaultRouter

app_name = 'events'

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')

urlpatterns = [
    path('', include(router.urls)),
    path('create/', EventCreateView.as_view(), name='event-create'),
    path('<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),
]
