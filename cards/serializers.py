from rest_framework import serializers
from .models import Card

class CardSerializer(serializers.ModelSerializer):
    tasks_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Card
        fields = [
            'id', 
            'title', 
            'description', 
            'category',
            'tasks_count'
        ]
        extra_kwargs = {
            'user': {'read_only': True},
        }
