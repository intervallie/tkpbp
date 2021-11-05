from django.urls import path
from .views import index, add_donasi, list_donasi

urlpatterns = [
    path('', index, name='index'),
    path('buat-donasi/', add_donasi, name='add_note'),
    path('list-donatur/', list_donasi, name='list_donasi'),
]
