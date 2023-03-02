from django.shortcuts import render


def index(request):
    data_for_main_page = {
        'title': 'Info security documents',
        'text': 'Информационная безопасность (ИБ) – это состояние информационной системы,'
                ' при котором она наименее восприимчива к вмешательству и нанесению ущерба со стороны третьих лиц.'
                'Безопасность данных также подразумевает управление рисками, которые связаны с разглашением информации'
                'или влиянием на аппаратные и программные модули защиты.Безопасность информации, которая обрабатывается'
                'в организации, – это комплекс действий, направленных на решение проблемы защиты информационной среды в'
                ' рамках компании. При этом информация не должна быть ограничена в использовании и динамичном развитии'
                'для уполномоченных лиц.',
    }
    return render(request, 'main/main.html', data_for_main_page)


def index_intro(request):
    return render(request, 'main/intro.html')


def index_docs(request):
    return render(request, 'main/docs.html')


def index_about(request):
    return render(request, 'main/about.html')


def index_other(request):
    return render(request, 'main/other.html')
