from django.shortcuts import render
from consultation_form.models import Consultation
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse


@login_required
def index(request):
    konsuls = Consultation.objects.all().values()
    response = {'konsuls' : konsuls}
    return render(request, 'konfirmasi_konsultasi.html', response)

def stringpurifier(words):
    newStr = ""
    for i in words:
        if i != " " or i != "\n":
            newStr += i
    return(" ".join(newStr.split()))    

@csrf_exempt
def delete_post(request):
    title=stringpurifier(request.POST.get("accept")) 
    try:
        Consultation.objects.get(title=title).delete()
        konsultasi_data={"error":False,"errorMessage":"Deleted Successfully", "accept":accept}
        return JsonResponse(konsultasi_data,safe=False)
    except:
        konsultasi_data={"error":True,"errorMessage":"Failed to Delete Data", "accept":accept}
        return JsonResponse(konsultasi_data,safe=False)

def accept(request):
    return render(request, 'accept.html')

def reject(request):
    return render(request, 'reject.html')
