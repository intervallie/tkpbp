from django.shortcuts import render
from .models import Consultation
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    konsuls = Consultation.objects.all().values()
    response = {'konsuls' : konsuls}
    return render(request, 'konfirmasi_konsultasi.html', response)


