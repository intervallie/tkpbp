from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, JsonResponse
from django.core import serializers
from accounts.models import Account
from consultation_form.forms import ConsForm

@login_required(login_url="/login", redirect_field_name=None)
def index(request):
    if (request.user.is_counselor):
        return render(request, "consultation_form_notcounselor.html")
    consultation_form = ConsForm()
    city_list = ['Jakarta',
                 'Bogor',
                 'Depok',
                 'Tangerang',
                 'Bekasi']
    response = {'consultation_form': consultation_form, 'city_list': city_list, 'nbar': 'Konsultasi'}
    return render(request, "consultation_form_index.html", response)

def get_counselor(request):
    # is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    # if (is_ajax and request.method == 'GET'):
    print("fetching counselor")
    counselor = Account.objects.filter(is_counselor=True)
    data = serializers.serialize('json', counselor)
    return HttpResponse(data, content_type='application/json')