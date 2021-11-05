from django.urls import path
from .views import index, thread_detail, add_thread, thread_list

urlpatterns = [
    path('', index, name='index'),
    path('<int:thread_id>', thread_detail),
    path('add-thread', add_thread),
    path('threads', thread_list),
]