from django import forms
from .models import Donasi


class DonasiForm(forms.ModelForm):
    class Meta:
        model = Donasi
        fields = "__all__"
        