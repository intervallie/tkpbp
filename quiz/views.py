from django.shortcuts import render

# Create your views here.
def quiz_start(request):
    return render(request, 'quiz-start.html')

def quiz(request):
    return render(request, 'quiz.html')