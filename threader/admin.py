from django.contrib import admin
from django.db import models
from .models import Thread, ThreadLike

# Register your models here.
class ThreadLikeAdmin(admin.TabularInline):
    model = ThreadLike

class ThreadAdmin(admin.ModelAdmin):
    inlines = [ThreadLikeAdmin]
    list_display = ['__str__', 'user']
    search_fields = ['content', 'user_username', 'user_email']
    class Meta:
        model = Thread

admin.site.register(Thread)