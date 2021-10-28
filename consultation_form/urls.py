from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('json', views.get_counselor, name='get_counselor'),
]