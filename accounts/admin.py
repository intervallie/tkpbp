from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import BioPsikolog
user = get_user_model()
admin.site.register(user)
admin.site.register(BioPsikolog)