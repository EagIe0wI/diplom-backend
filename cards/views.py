from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework import viewsets
from .models import Card
from .serializers import CardSerializer

class CardListView(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    # permission_classes = [IsAuthenticated]

class CardDetailView(RetrieveAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)

class CardCreateView(CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)

class CardUpdateView(UpdateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)

class CardDeleteView(DestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)
