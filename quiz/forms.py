from django import forms
from django.forms import fields
from .models import suggestion

class suggestionForm(forms.ModelForm):
    class Meta:
        model = suggestion
        fields=[
            'Saran'
        ]
