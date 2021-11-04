from django.shortcuts import render
from .models import suggestion
from .forms import suggestionForm
from django.http import HttpResponseRedirect
# Create your views here.
def quiz_start(request):
    response={'nbar':'Quiz'}
    return render(request, 'quiz-start.html',response)

def quiz(request):
    return render(request, 'quiz.html')

def hasil(request):
    return render(request, 'sedang.html')

def form(request):
    form = suggestionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/artikel/')
    response = {
        'form':form,
        'nbar':'Quiz'
    }
    return render(request,'form.html',response)

def saran(request):
    if request.user.is_authenticated and request.user.is_staff:
        saran = suggestion.objects.all()
        response ={'nbar':'Quiz', 'suggestion': saran}
        return render(request,'saran.html',response)
    
    return HttpResponseRedirect('/artikel/')
