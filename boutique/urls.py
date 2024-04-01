from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . views import ProduitViewSet, CategorieViewset

route = DefaultRouter()

route.register('produits', ProduitViewSet, 'produit')

route.register('categories', CategorieViewset, 'categorie')


urlpatterns = [
    path('', include(route.urls))
]