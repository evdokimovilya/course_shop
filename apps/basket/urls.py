from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.basket, name='basket'),
    path('add/<int:course_id>', views.basket_add, name='basket_add'),
    path('remove/<int:course_id>', views.basket_remove, name='basket_remove')
    
]
