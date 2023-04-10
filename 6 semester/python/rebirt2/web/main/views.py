from django.shortcuts import render


def index_main(request):
    data_for_main = {
        'title': 'Economical info security - твой помощник при выборе оборудования, для построения '
                 'защищенных систем',
    }
    return render(request, 'main/main.html', data_for_main)

def index_about(request):
    return render(request, 'main/about.html')


