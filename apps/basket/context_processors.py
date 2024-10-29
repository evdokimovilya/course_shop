from django.conf import settings

from apps.basket.models import Basket


def basket(request):
    if request.user.is_authenticated:
        user = request.user
        basket = Basket.objects.filter(owner=user, status=Basket.StatusChoices.OPEN).first()
    else:
        basket = None
    return {
        "basket": basket
    }