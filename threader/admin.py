from django.contrib import admin
from django.db import models
from .models import Thread

# Register your models here.
class ThreadAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user_username', 'user_email']
    class Meta:
        model = Thread

admin.site.register(Thread)