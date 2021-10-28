from django.urls import path
from .views import quiz_start, quiz, hasil
urlpatterns = [
    path('', quiz_start, name='quiz start'),
    path('quiz/', quiz, name='quiz'),
    path('hasil/',hasil, name='hasil')
]