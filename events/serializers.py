from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id', 
            'title', 
            'description', 
            'date_happened',
            'card',
        ]
        extra_kwargs = {'user': {'read_only': True}}
