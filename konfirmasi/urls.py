from django.urls import path
from django.contrib import admin

from article.views import delete_post
from .views import index, accept, reject, delete_post

urlpatterns = [
    path('', index, name='index'),
    path('accept', accept, name='accept'),
    path('reject', reject, name='reject'),
    path('delete_post', delete_post, name='delete_post'),
]