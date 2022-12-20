from rest_framework import serializers
from .models import TodoItem
import json



class TodoListSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=200)
    done = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return TodoItem(**validated_data)