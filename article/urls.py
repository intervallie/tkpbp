from django.urls import include, path
from .views import index, singlePost, add_article, adminView, delete_post, edit_post
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('', index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)