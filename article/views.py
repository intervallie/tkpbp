from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user, login, logout,authenticate

def stringpurifier(words):
    newStr = ""
    for i in words:
        if i != " " or i != "\n":
            newStr += i
    return(" ".join(newStr.split()))

# Create your views here.
def index(request):
    article = Article.objects.all().values()
    response = {'article':article,'nbar':'Artikel'}
    return render(request, 'article_index.html', response)


def add_article(request):
    if request.user.is_authenticated and (request.user.is_counselor or request.user.is_staff or request.user.is_superuser):
        form = ArticleForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('..')
        return render(request, "article_add.html", {'form': form})
    else:
        return redirect('../artikel')

def singlePost(request, id):
    post = Article.objects.get(id=id)
    response = {'post':post}
    return render(request, "single_article.html", response)

def adminView(request):
    if request.user.is_authenticated and (request.user.is_counselor or request.user.is_staff or request.user.is_superuser):
        article = Article.objects.all().values()
        response = {'article':article}
        return render(request, 'admin_view.html', response)
    else:
        return redirect('../artikel')
    
@csrf_exempt
def delete_post(request):
    title=stringpurifier(request.POST.get("title")) 
    try:
        Article.objects.get(title=title).delete()
        article_data={"error":False,"errorMessage":"Deleted Successfully", "title":title}
        return JsonResponse(article_data,safe=False)
    except:
        article_data={"error":True,"errorMessage":"Failed to Delete Data", "title":title}
        return JsonResponse(article_data,safe=False)

def edit_post(request, id):
    if request.user.is_authenticated and (request.user.is_counselor or request.user.is_staff or request.user.is_superuser):
        post = Article.objects.get(id=id)
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return adminView(request)
        else:
            form = ArticleForm(instance=post)
        return render(request, "article_add.html", {'form': form})
    else:
        return redirect('../artikel')

