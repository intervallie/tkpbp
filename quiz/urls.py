from django.urls import path
from .views import quiz_start, quiz
urlpatterns = [
    path('', quiz_start, name='quiz start'),
    path('quiz/', quiz, name='quiz')
]