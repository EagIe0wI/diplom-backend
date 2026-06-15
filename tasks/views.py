from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import viewsets, filters
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter] 
    search_fields = ['title'] 

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)
        card_id = self.request.query_params.get('card')
        if card_id is not None:
            queryset = queryset.filter(card=card_id)
        return queryset
    
    @action(detail=False, methods=['get'])
    def today(self, request):
        """Возвращает задачи на день, переданный фронтендом, и их счетчик"""
        client_date_str = request.query_params.get('date')
        
        if client_date_str:
            from datetime import datetime
            client_date = datetime.strptime(client_date_str, '%Y-%m-%d')
        else:
            client_date = timezone.now()
            
        today_start = client_date.replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = client_date.replace(hour=23, minute=59, second=59, microsecond=999999)
        
        queryset = Task.objects.filter(
            user=request.user,
            start_date__range=(today_start, today_end)
        )
        
        active_count = queryset.exclude(status='done').count()
        
        serializer = self.get_serializer(queryset, many=True)
        
        return Response({
            'count': active_count,
            'results': serializer.data
        })
    
    @action(detail=False, methods=['get'])
    def overdue(self, request):
        """Возвращает невыполненные задачи, дедлайн которых прошёл, и их счетчик"""
        client_date_str = request.query_params.get('date')
        
        if client_date_str:
            from datetime import datetime
            client_date = datetime.strptime(client_date_str, '%Y-%m-%d')
        else:
            client_date = timezone.now()
            
        today_start = client_date.replace(hour=0, minute=0, second=0, microsecond=0)
        
        queryset = Task.objects.filter(
            user=request.user,
            start_date__lt=today_start,
            status='todo'
        )
        
        serializer = self.get_serializer(queryset, many=True)
        
        return Response({
            'count': queryset.count(),
            'results': serializer.data
        })


    
class TaskCreateView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
class TaskUpdateView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
        
class TaskDeleteView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
