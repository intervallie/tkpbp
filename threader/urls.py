from django.urls import path
from .views import index, thread_detail, add_thread, thread_list, thread_delete, thread_action

urlpatterns = [
    path('', index, name='index'),
    path('<int:thread_id>', thread_detail),
    path('<int:thread_id>/delete', thread_delete),
    path('add-thread', add_thread),
    path('threads', thread_list),
    path('action', thread_action),
]