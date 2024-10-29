from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status

from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.basket.models import Line

from .serializers import BasketSerializer, BasketLinesSerializer

@api_view()
def basket(request):
    basket = request.basket
    data = BasketLinesSerializer(basket.basket_lines.all(), many=True).data

    return Response(data)


@api_view(['DELETE'])
def basket_remove(request, item_id): 
    try:
        basket_item = Line.objects.get(pk=item_id) 
        basket_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    except ObjectDoesNotExist:
        return Response({'detail': 'Элемент не найден.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'detail': f'Произошла ошибка: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
