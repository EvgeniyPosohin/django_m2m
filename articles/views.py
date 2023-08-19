from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    content = Article.objects.order_by('-published_at').all()
    context = {'object_list': content}
    return render(request, template, context)
