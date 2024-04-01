from django.contrib import admin

# Register your models here.

from . models import Produit, Categorie



admin.site.register(Produit)

admin.site.register(Categorie)
