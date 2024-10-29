from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('basket', views.basket, name='basket_api'),
    # path('basket/<int:course_id>', views.basket_add, name='basket_add'),
    path('basket/<int:item_id>/', views.basket_remove, name='basket_remove')
]
