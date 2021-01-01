from django.shortcuts import render, get_object_or_404
from .models import Article


def articles(request):
    articles = Article.objects.order_by('-date')
    return render(request, 'blog/index.html', {'articles': articles})


def article_details(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/article_details.html', {'article': article})
