from django.shortcuts import render
from .models import Konsultasi
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    konsuls = Konsultasi.objects.all().values()
    response = {'konsuls' : konsuls}
    return render(request, 'konfirmasi_konsultasi.html', response)

def accept(request):
    return render(request, 'accept.html')

def reject(request):
    return render(request, 'reject.html')
