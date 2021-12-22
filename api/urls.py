from django.urls import include, path, re_path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)




urlpatterns = [
    path('token/',MyTokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(),name='token_refresh'),
    path('konfirmasi', KonfirmasiAPI.as_view(), name = 'konfirmasi'),
    # re_path(r'^artikel/(?P<pk>\d+)/$', ArticleList.as_view(),name = 'artikel'),
    path('artikel',ArticleAPI.as_view(),name = 'artikel-get'),
    path('artikel/<int:pk>',ArticleAPI.as_view(),name = 'artikel-other'),
    path('artikel/photo',PhotoAPI.as_view(),name = 'photo'),
    path('saran',SuggestionAPI.as_view(),name = 'saran'),
    path('konsultasi',ConsultationAPI.as_view(), name = 'konsultasi'),
    path('donasi',DonasiAPI.as_view(), name = 'donasi')
]