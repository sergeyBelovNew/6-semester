from django.shortcuts import render, redirect
from .models import Equipment
from .forms import EquipmentForm
from django.views.generic import DetailView, UpdateView, DeleteView


def index_main(request):
    equipment = Equipment.objects.all()
    dict_equipment = {'equipment': equipment}
    return render(request, 'calculator/main.html', dict_equipment)


def index_create(request):
    exception = ""
    if request.method == "POST":
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            exception = "Ошибка формы"

    form = EquipmentForm()
    data = {
        'form': form,
        'exception': exception
    }
    return render(request, "calculator/create.html", data)


class NewsDetailView(DetailView):
    model = Equipment
    template_name = 'calculator/details_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Equipment
    template_name = 'calculator/create.html'

    form_class = EquipmentForm


class NewsDeleteView(DeleteView):
    model = Equipment
    success_url = 'calculator/'
    template_name = 'calculator/calculator-delete.html'
