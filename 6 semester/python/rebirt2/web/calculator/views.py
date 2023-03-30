from django.shortcuts import render, redirect
from .models import Equipment
from .forms import EquipmentForm
from django.views.generic import DetailView, UpdateView, DeleteView

import sys

sys.path.append("..")

from cart.forms import CartAddEquipmentForm

def index_main(request):
    equipment = Equipment.objects.all()
    сart_add_equipment_form = CartAddEquipmentForm
    dict_equipment = {'сart_add_equipment_form': сart_add_equipment_form, 'equipment': equipment}

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


class CalculatorDetailView(DetailView):
    model = Equipment
    template_name = 'calculator/details_view.html'
    context_object_name = 'article'


class CalculatorUpdateView(UpdateView):
    model = Equipment
    template_name = 'calculator/create.html'

    form_class = EquipmentForm


class CalculatorDeleteView(DeleteView):
    model = Equipment
    success_url = '../'
    template_name = 'calculator/calculator-delete.html'
