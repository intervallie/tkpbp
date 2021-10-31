from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import get_user, login, logout,authenticate
from accounts.forms import *
from django.contrib.auth.views import LoginView


# Create your views here.
def base_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('home')
    else:
        return HttpResponseRedirect('login')

def signup_mahasiswa(request):
    context = {}
    if request.method == 'POST':
        form = MyUserForm(data =request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            context['registration_form'] = form
   
    form = MyUserForm()
    context['form'] = form
    return render(request,'signup.html',context)

def signup_psikolog(request):
    context = {}
    if request.method == 'POST':
        form = MyUserForm(request.POST)
        form.set_psikolog_status(True)
        biodata_form = MyPsikologForm(request.POST)
        if form.is_valid() and biodata_form.is_valid():
            user = form.save()
            biodata = biodata_form.save(commit=False)
            biodata.user = user
            biodata.save()

            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            context['error_user_form'] = form
            context['error_biodata_form'] = biodata_form
    else:
        form = MyUserForm()
        biodata_form = MyPsikologForm()
    context['form'] = form
    context['biodata_form'] = biodata_form
    return render(request,'signup_psikolog.html',context)

def login_view(request):
    context = {}
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return HttpResponseRedirect('artikel')

    else:
        form = AuthenticationForm()
    
    form.fields['username'].widget.attrs.update({'placeholder': 'Email','class':'form-control'})
    form.fields['password'].widget.attrs.update({'placeholder': 'Password','class':'form-control'})
    context['form'] = form
    context['nbar'] = 'login'
    return render(request,'login.html',context)

def home_view(request):
    if request.user.is_authenticated:
        return render(request,'halo.html')
    else:
        return render(request,'bisagila.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('login')

def registrasi_view(request):
    return render(request,'registrasi.html', {'nbar' : 'Registrasi'})

def profil_view(request):
    if request.user.is_authenticated:
        return render(request,'profil.html')
    return render(request,'bisagila.html')

# Untuk liat base
def basetemp_view(request):
    return render(request,'base.html',{'nbar' : 'base'})


    