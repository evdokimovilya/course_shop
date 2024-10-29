
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('preview', views.preview, name='checkout_preview'),
    path('success', views.success, name='checkout_success')

]
