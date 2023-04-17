import sys

from django.shortcuts import render
from django.views.generic import DetailView


sys.path.append("..")
from docs.models import GeneralDocument



# Create your views here.
def index_general_docs(request):
    docs = GeneralDocument.objects.all()
    dict_docs = {'docs': docs}
    return render(request, 'docs/main.html', dict_docs)



class GeneralDocsDetailView(DetailView):
    model = GeneralDocument
    template_name = 'docs/detail.html'
    context_object_name = 'article'
