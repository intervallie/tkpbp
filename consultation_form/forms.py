from django.db.models import fields
from django.forms import ModelForm
from django.forms.widgets import DateInput, TextInput
from consultation_form.models import Consultation
from datetime import date

class ConsForm(ModelForm):
    class Meta:
        model = Consultation
        fields = ('full_name', 'npm', 'date', 'email')
        widgets = {'full_name': TextInput(attrs={'class': 'form-control border-dark mb-5'}),
                   'npm': TextInput(attrs={'class': 'form-control border-dark mb-5'}),
                   'date': DateInput(attrs={'class': 'form-control border-dark mb-5', 'type': 'date', 'min': date.today().strftime("%Y-%m-") + "{:0>2}".format(str((int(date.today().strftime("%d")) + 1)))}),
                   'email': TextInput(attrs={'class': 'form-control border-dark mb-5'})}