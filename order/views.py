from django.shortcuts import render

from . models import *

from rest_framework import viewsets

from . serializers import *


class OrderViewSet(viewsets.ModelViewSet):
    
    queryset = Order.objects.all()
    
    serializer_class = OrderSerializer
    