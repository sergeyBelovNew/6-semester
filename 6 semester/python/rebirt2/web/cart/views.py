
from django.shortcuts import render, get_object_or_404, redirect

from django.views.decorators.http import require_POST

import sys
from .cart import Cart
from .forms import CartAddProductForm

sys.path.append("..")
from calculator.models import Equipment


@require_POST
def add_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Equipment, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('calculator')


def remove_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Equipment, id=product_id)
    cart.remove(product)
    return redirect('cart:detail_cart')


def detail_cart(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

