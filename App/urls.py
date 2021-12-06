from os import name
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('paymenthandler/', paymenthandler, name="paymenthandler"),
]
