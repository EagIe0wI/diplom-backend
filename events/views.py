from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer

class EventListView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # permission_classes = [IsAuthenticated]

class EventDetailView(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)

class EventCreateView(CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)

class EventUpdateView(UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)

class EventDeleteView(DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Event.objects.filter(user=self.request.user)
