from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from . models import Produit, Categorie

from . serializers import ProduitSerializer, CategorieSerializer

class CategorieViewset(viewsets.ModelViewSet):
    
    queryset = Categorie.objects.all()
    
    serializer_class = CategorieSerializer


class ProduitViewSet(viewsets.ModelViewSet):
    
    queryset = Produit.objects.all()
    
    serializer_class = ProduitSerializer
