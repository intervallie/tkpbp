from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    article = Article.objects.all().values()
    response = {'article':article,'nbar':'Artikel'}
    return render(request, 'article_index.html', response)

#@login_required(login_url='')
def add_article(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('..')
    return render(request, "article_add.html", {'form': form})

def singlePost(request, id):
    post = Article.objects.get(id=id)
    response = {'post':post}
    return render(request, "single_article.html", response)

#@login_required(login_url='')
def adminView(request):
    article = Article.objects.all().values()
    response = {'article':article}
    return render(request, 'admin_view.html', response)

def delete_post(request, id):
    post = Article.objects.get(id=id)
    post.delete()
    return adminView(request)

def edit_post(request, id):
    post = Article.objects.get(id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return adminView(request)
    else:
        form = ArticleForm(instance=post)
    return render(request, "article_add.html", {'form': form})