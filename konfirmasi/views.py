from django.shortcuts import render
from consultation_form.models import Consultation
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    konsuls = Consultation.objects.all().values()
    response = {'konsuls' : konsuls,'nbar' : 'Konfirmasi'}
    return render(request, 'konfirmasi_konsultasi.html', response)

def accept(request):
    return render(request, 'accept.html')

def reject(request):
    return render(request, 'reject.html')
