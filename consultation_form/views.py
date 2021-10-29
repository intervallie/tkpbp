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

def get_counselor(request, city=None):
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    if (is_ajax and request.method == 'GET' and city == 'Jakarta'):
        counselor = Account.objects.filter(is_counselor=True)
        data = serializers.serialize('json', counselor)
        return HttpResponse(data, content_type='application/json')
    else:
        return JsonResponse({}, status=404)

def submit_form(request, pk_counselor):
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    if (is_ajax and request.method == 'POST'):
        print("trying to submit form")
        counselorInstance = Account.objects.get(pk=pk_counselor)
        # Get the form data and create object ConsForm
        form = ConsForm(request.POST)
        if form.is_valid():
            # Create instance but dont save it yet
            save_form = form.save(commit=False)
            # Assign counselor to form
            save_form.selected_counselor = counselorInstance
            # Save the form
            save_form.save()
            # Return response success
            return JsonResponse({}, status=200)
        else :
            # If form is not valid then return response submit error
            return JsonResponse({}, status=400)

    # if not ajax or request is not post then return error
    return JsonResponse({}, status=400)