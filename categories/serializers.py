from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'title', 
            'description', 
        ]
        extra_kwargs = {
            'user': {'read_only': True},
        }
