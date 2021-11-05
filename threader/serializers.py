from django.conf import settings
from rest_framework import serializers
from .models import Thread

MAX_THREAD_LENGTH = settings.MAX_THREAD_LENGTH

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = ["content"]

    def validate(self, value):
        if len(value) > MAX_THREAD_LENGTH:
            raise serializers.ValidationError("This thread is too long")
        return value