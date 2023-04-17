from django.shortcuts import render


def index_main(request):
    data_for_main = {
        'title': 'Цель проекта',
        'text': 'Данный сайт создан для помощи пользователям в обзоре и поиске документов по Иноформационной безопасности'
                 ', а также в подборе нужного оборудования для защиты информационной системы',
    }
    return render(request, 'main/main.html', data_for_main)

def index_about(request):
    return render(request, 'main/about.html')


