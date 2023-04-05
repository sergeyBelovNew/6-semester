from django.shortcuts import render


def index_main(request):
    data_for_main = {
        'title': 'Данный сайт предназначен для проведения расчетов затрат на построение защинных информационных систем',
    }
    return render(request, 'main/main.html', data_for_main)


def index_general_docs(request):
    data_docs = {
    }
    return render(request, 'main/general_docs.html', data_docs)


def index_about(request):
    return render(request, 'main/about.html')


