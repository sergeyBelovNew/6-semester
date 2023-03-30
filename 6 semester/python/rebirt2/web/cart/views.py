from django.core.checks import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST

import sys
from .cart import Cart
from .forms import CartAddEquipmentForm

sys.path.append("..")
from calculator.models import Equipment


@require_POST
@require_POST
def add_to_cart(request, equipment_id):
    cart = Cart(request)
    equipment = get_object_or_404(Equipment, id=equipment_id)
    form = CartAddEquipmentForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(equipment=equipment, quantity=cd['quantity'],
                 update_quantity=cd['update']                 )
    return redirect('cart:detail_cart')


def remove_cart(request, equipment_id):
    cart = Cart(request)
    equipment = get_object_or_404(Equipment, id=equipment_id)
    cart.remove(equipment)
    return redirect('cart:detail_cart')


def detail_cart(request):
    cart = Cart(request)
    dict_cart = {'cart': cart}
    return render(request, 'cart/detail.html', dict_cart)
