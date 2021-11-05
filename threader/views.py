import json
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils.http import is_safe_url
from django.conf import settings
from django.shortcuts import render, redirect
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Thread
from .forms import ThreadForm
from django.contrib.auth.decorators import login_required
from .serializers import ThreadSerializer

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def index(request, *args, **kwargs):
    thread = Thread.objects.all().values()
    response = {'thread':thread,'nbar':'Diskusi'}
    return render(request, 'threader.html', response, status=200)

@api_view(['GET'])
def thread_list(request, *args, **kwargs):
    qs = Thread.objects.all()
    serializer = ThreadSerializer(qs, many=True)
    return Response(serializer.data, status=200)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_thread(request, *args, **kwargs):
    serializer = ThreadSerializer(data=request.POST or None)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)

@api_view(['GET'])
def thread_detail(request, thread_id, *args, **kwargs):
    qs = Thread.objects.filter(id=thread_id)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = ThreadSerializer(obj)
    return Response(serializer.data, status=200)

def thread_list_pure_django(request, *args, **kwargs):
    qs = Thread.objects.all()
    thread_list = [x.serialize() for x in qs]
    data = {
        "isUser": False,
        "response": thread_list
    }
    return JsonResponse(data)

def add_thread_pure_django(request, *args, **kwargs):
    user = request.user
    if not request.user.is_authenticated:
        user = None
        if request.is_ajax():
            return JsonResponse({}, status=401)
        return redirect(settings.LOGIN_URL)
    # create object of form
    form = ThreadForm(request.POST or None, request.FILES or None)
    next_url = request.POST.get("next") or None

    # check if request method is POST and form data is valid  
    if request.method == "POST" and form.is_valid():
        # save the form data to model
        obj = form.save(commit=False)
        obj.user = user
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201)
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect('/threader/')
        form = ThreadForm()
    if form.errors and request.is_ajax:
        return JsonResponse(form.errors, status=400)
    return render(request, "forms.html", context={"form": form})

def thread_detail_pure_django(request, thread_id, *args, **kwargs):
    data = {
        "id": thread_id,
    }
    status = 200
    try:
        obj = Thread.objects.get(id=thread_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404
    return JsonResponse(data, status=status)