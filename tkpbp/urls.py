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
from article.views import index as index_article
import article.urls as article
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', index_article, name='index'),
    path('views/<int:id>', article.singlePost, name='singlePost'),
    path('add', article.add_article, name='add'),
    path('admin_view', article.adminView, name='admin_view'),
    path('delete/<int:id>', article.delete_post, name='delete'),
    path('edit/<int:id>', article.edit_post, name='edit'),
    path('consultation/', include('consultation_form.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)