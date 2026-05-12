from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework import viewsets
from .models import Tag
from .serializers import TagSerializer

class TagListView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    # permission_classes = [IsAuthenticated]

class TagDetailView(RetrieveAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)

class TagCreateView(CreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)

class TagUpdateView(UpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)

class TagDeleteView(DestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Tag.objects.filter(user=self.request.user)
