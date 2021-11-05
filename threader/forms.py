from django import forms
from .models import Thread
from django.conf import settings

MAX_THREAD_LENGTH = settings.MAX_THREAD_LENGTH

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ["content"]

    def validate(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_THREAD_LENGTH:
            raise forms.ValidationError("This thread is too long")
        return content