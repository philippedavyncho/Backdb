from django.db import models
from boutique.models import Produit 

        
class Order(models.Model):
    
    nom = models.CharField(max_length=255)
    
    phone = models.CharField(max_length=10)
    
    produit = models.ForeignKey(Produit, related_name='produit', on_delete=models.CASCADE)
    
    quantity = models.IntegerField(default=1)
    
    nom_vendeur = models.CharField(max_length=255)  # Champ pour le nom du vendeur du produit dans la commande

    def save(self, *args, **kwargs):
        # Associer le nom du vendeur du produit à la commande
        if self.produit:
            self.nom_vendeur = self.produit.nom_vendeur
        super().save(*args, **kwargs)

    def __str__(self):
        return f"nom: {self.produit.name}, quantité: {self.quantity}, prix: {self.produit.price * self.quantity}, vendeur: {self.nom_vendeur}"
    
    
        
        

    
        
    
    
    
