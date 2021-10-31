from django.urls import path
from django.contrib import admin
from .views import index, accept, reject

urlpatterns = [
    path('', index, name='index'),
    path('accept', accept, name='accept'),
    path('reject', reject, name='reject'),
]