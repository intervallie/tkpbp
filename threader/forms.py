from django import forms
from .models import Thread

MAX_THREAD_LENGTH = 280

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ["content"]

    def validate(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_THREAD_LENGTH:
            raise forms.ValidationError("This thread is too long")
        return content