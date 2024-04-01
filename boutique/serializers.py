from rest_framework import serializers
from . models import Categorie, Produit

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'


class ProduitSerializer(serializers.ModelSerializer):
    
    categorie = CategorieSerializer()
    
    class Meta:
        
        model = Produit
        
        fields = '__all__'