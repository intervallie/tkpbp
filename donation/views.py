from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Donasi
from .forms import DonasiForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    donasi = Donasi.objects.all().values()
    response = {'donasi': donasi,'nbar':'Donasi'}
    return render(request, 'donasi_index.html', response)

def add_donasi(request):
    form = DonasiForm()
    if request.method == 'POST':
        form = DonasiForm(request.POST or None, request.FILES or None)
        if request.is_ajax():
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/donasi')
        return HttpResponseRedirect('/donasi')
    response = {'form': form}
    return render(request, 'donasi_add.html', response)

@login_required(login_url='/admin/login/')
def list_donasi(request):
    donasi = Donasi.objects.all().values()
    response = {'donasi':donasi}
    return render(request, 'list_donasi.html', response)
