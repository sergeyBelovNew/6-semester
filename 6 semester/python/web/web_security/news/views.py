from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm
from django.views.generic import DetailView


def index_news(request):
    news = Document.objects.all()
    dict_news = {'news': news}
    return render(request, "news/news_home.html", dict_news)


def index_create(request):
    exception = ""
    if request.method == "POST":
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            exception = "Ошибка формы"

    form = DocumentForm()
    data = {
        'form': form,
        'exception': exception
    }
    return render(request, "news/create.html", data)


class NewsDetailView(DetailView):
    model = Document
    template_name = 'news/details_view.html'
    context_object_name = 'article'
