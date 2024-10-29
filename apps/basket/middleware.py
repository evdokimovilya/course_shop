
from apps.basket.models import Basket

class BasketMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        basket_id = request.session.get('basket_id')

        if basket_id:
            basket = Basket.objects.get(pk=basket_id)
        else:
            basket = Basket.objects.create()

        if request.user.is_authenticated:
            if not basket.owner:
                self.close_old_baskets(basket, request.user)
                
                basket.owner = request.user
                basket.save()
                
        request.session['basket_id'] = basket.id 
        request.basket = basket

        response = self.get_response(request)
        return response
    
    def close_old_baskets(self, basket, user):
        user.user_baskets.filter(status=Basket.StatusChoices.OPEN).update(status=Basket.StatusChoices.SUBMITTED)
            