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
    form = ArticleForm(request.POST, request.FILES or None)
    if form.is_valid():
        form.save()
    return render(request, "article_add.html", {'form': form})

def singlePost(request, id):
    post = Article.objects.get(id=id)
    response = {'post':post}
    return render(request, "single_article.html", response)