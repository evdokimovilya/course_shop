from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from apps.course.models import Course

from . models import Line



def basket_add(request, course_id):

    course  = get_object_or_404(Course, id=course_id)
    basket = request.basket
    Line.objects.get_or_create(course=course, price=course.price, basket=basket)

    return JsonResponse({'total_items': len(basket.basket_lines.all())})
    

def basket_remove(request, course_id):

    basket = request.basket
    basket.basket_lines.filter(course_id=course_id).delete()

    return JsonResponse({})



def basket(request):
    basket = request.basket

    return render(request, 'basket/detail.html', {'basket': basket})