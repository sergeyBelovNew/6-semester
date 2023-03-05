from django.shortcuts import render
from .models import Document


def index_news(request):
    news = Document.objects.all()
    dict_news = {'news':  news}
    return render(request, "news/news_home.html", dict_news)
