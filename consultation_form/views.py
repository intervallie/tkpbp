from django.shortcuts import render
from consultation_form.forms import ConsForm

# Create your views here.
def index(request):
    consultation_form = ConsForm()
    city_list = ['Jakarta',
                 'Bogor',
                 'Depok',
                 'Tangerang',
                 'Bekasi']
    response = {'consultation_form': consultation_form, 'city_list': city_list, 'nbar': 'Konsultasi'}
    return render(request, "consultation_form_index.html", response)