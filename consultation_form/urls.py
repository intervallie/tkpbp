from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('json/<str:city>', views.get_counselor, name='get_counselor'),
    path('submit/<int:pk_counselor>', views.submit_form, name='submit_form')
]