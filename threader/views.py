from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from .models import Thread
from .forms import ThreadForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request, *args, **kwargs):
    thread = Thread.objects.all().values()
    response = {'thread':thread,'nbar':'Diskusi'}
    return render(request, 'threader.html', response, status=200)

def add_thread(request, *args, **kwargs):
    context = {}
    # create object of form
    form = ThreadForm(request.POST or None, request.FILES or None)
    next_url = request.POST.get("next") or None

    # check if request method is POST and form data is valid  
    if request.method == "POST" and form.is_valid():
        # save the form data to model
        obj = form.save(commit=False)
        obj.save()
        if next_url != None:
            return redirect('/threader/')
        form = ThreadForm()
    context['form'] = form
    return render(request, "forms.html", context={"form": form})

def thread_detail(request, thread_id, *args, **kwargs):
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