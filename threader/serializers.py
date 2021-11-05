from django.conf import settings
from rest_framework import serializers
from .models import Thread

MAX_THREAD_LENGTH = settings.MAX_THREAD_LENGTH
THREAD_ACTION_OPTIONS = settings.THREAD_ACTION_OPTIONS

class ThreadActionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    action = serializers.CharField()

    def validate_action(self, value):
        value = value.lower().strip()
        if not value in THREAD_ACTION_OPTIONS:
            raise serializers.ValidationError("This is not a valid action for threads")
        return value

class ThreadSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Thread
        fields = ['id', 'content', 'likes']

    def get_likes(self, obj):
        return obj.likes.count()

    def validate(self, value):
        if len(value) > MAX_THREAD_LENGTH:
            raise serializers.ValidationError("This thread is too long")
        return value