# pages/urls.py

from django.urls import path
from .views import client_form_view, success_view, print_receipt

urlpatterns = [
    path('', client_form_view, name='client_form'),
    path('success/', success_view, name='success'),
    path('print-receipt/<int:client_id>/', print_receipt, name='print_receipt'),
]
