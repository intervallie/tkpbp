from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, JsonResponse
from django.core import serializers
from accounts.models import Account
from consultation_form.forms import ConsForm
from accounts.models import BioPsikolog
import json

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
    psikolog_list = BioPsikolog.objects.all()
    response = {'consultation_form': consultation_form, 
                'city_list': city_list,
                'psikolog_list' : psikolog_list, 
                'nbar': 'Konsultasi'
                }
    return render(request, "consultation_form_index.html", response)

def get_counselor(request, city):
    print("get_counselor activated")
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    if (is_ajax and request.method == 'GET'):
        counselor = Account.objects.filter(is_counselor=True,biopsikolog__domisili=city)
        counselor_bio = BioPsikolog.objects.filter(user__is_counselor=True,domisili=city)
        print(counselor)
        print(counselor_bio)
        counselor_object = [*counselor,*counselor_bio]
        print(type(counselor_object))
        data = serializers.serialize('json', counselor_object)
        print(data)
        print(type(data))
        data_sebar = {'akun_psikolog':data}
        print(data_sebar)
        return HttpResponse(data, content_type='application/json')
    else:
        return HttpResponse("{}", content_type='application/json')