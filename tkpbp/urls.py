"""tkpbp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path, re_path
from django.contrib import admin
from article.views import index as index_konfirmasi
import article.urls as article
import accounts.urls as accounts
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('konfirmasi/', include('konfirmasi.urls')),
    path('',include(accounts)),
    path('artikel/', include(('article.urls','article'), namespace='article')),
<<<<<<< HEAD
<<<<<<< HEAD
    re_path(r'^$', index_konfirmasi, name='index'),
=======
=======
>>>>>>> 7fb4f5bad6c4fc9ac7d5c8c2ea3d943bd53092f4
    path('consultation/', include(('consultation_form.urls', 'consultation_form'), namespace='consultation_form')),
    # re_path(r'^$', index_article, name='index'),
>>>>>>> 7fb4f5bad6c4fc9ac7d5c8c2ea3d943bd53092f4


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)