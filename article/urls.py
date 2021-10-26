from django.urls import include, path
from .views import index, singlePost, add_article
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('', index, name='index'),
    #path('add', add_article, name='add'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)