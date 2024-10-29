from django.shortcuts import render, redirect
from django.http import Http404

from apps.basket.models import Basket

from . models import Order


def preview(request):
    basket = request.basket

    if request.method == 'POST':
        order = Order.objects.create(basket=basket, user=request.user)

        basket.status = Basket.StatusChoices.SUBMITTED
        basket.save()

        request.session['checkout_order'] = order.pk
        del request.session['basket_id']

        return redirect('checkout_success')
    
    if request.user.is_authenticated:
        return render(request, 'checkout/preview.html', {'basket': basket})
    else:
        return redirect('login')


def success(request):
    
    order_pk = request.session.get('checkout_order')
    if order_pk:
        order = Order.objects.get(pk=order_pk)
        
        return render(request, 'checkout/success.html', {'order': order})
    
    raise Http404

