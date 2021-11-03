from django.urls import include, path
from .views import index, singlePost, add_article, adminView, delete_post, edit_post
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('', index, name='index'),
    path('add', add_article, name='add'),
    path('artikel/<int:id>', singlePost, name='singlePost'),

    path('admin_view', adminView, name='admin_view'),
    path('delete_post', delete_post, name='delete_post'),
    path('edit/<int:id>', edit_post, name='edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)