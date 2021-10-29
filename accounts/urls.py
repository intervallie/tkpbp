from django.contrib import admin
from django.urls import include, path, re_path
from .views import *
import article.views as article
urlpatterns = [
    path('',base_view,name='base'),
    path('login',login_view,name='login'),
    path('home',home_view,name='home'),
    path('signup',signup_mahasiswa,name='signup'),
    path('logout',logout_view,name='logout'),
    path('base',basetemp_view,name='basetemp'),
    path('registrasi',registrasi_view,name='registrasi'),
    path('registrasi/psikolog',signup_psikolog,name='psikolog'),
]
