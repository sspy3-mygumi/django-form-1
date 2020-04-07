from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Article
from .forms import ArticleForm

def index(request):
    # Article.objects.all()[::-1] -> Python
    articles = Article.objects.order_by('-pk') # Query문이 다름
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        # request.POST -> QueryDict
        # 변수 이름 = 클래스()  -> 클래스로부터 인스턴스 생성
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        # 비어있는 form
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/form.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # article = Article.objects.get(pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

# 주소창을 통해 ->  articles/2/delete/ -> GET
@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')

def update(request, article_pk):
    # 공통으로 사용
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        # request.POST -> QueryDict / article -> 기존 글
        # instance=article을 안넣어주면? -> 새로운 글이 작성됨
        form = ArticleForm(request.POST, instance=article)
        # print(form)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        # 기존에 사용자가 작성한 글이 포함된 == instance=article
        # Form
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/form.html', context)

