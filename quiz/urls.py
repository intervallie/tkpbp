from django.urls import path
from .views import quiz_start, quiz, hasil ,form, saran
urlpatterns = [
    path('quiz_start1/', quiz_start, name='quiz start'),
    path('quiz/', quiz, name='quiz'),
    path('hasil/',hasil, name='hasil'),
    path('saran/',form, name='form'),
    path('list-saran/',saran, name='lihat saran')
]