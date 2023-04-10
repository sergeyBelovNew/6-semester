from django.shortcuts import render

# Create your views here.
def index_general_docs(request):
    data_docs = {
    }
    return render(request, 'docs/main.html', data_docs)
