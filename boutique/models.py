from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Categorie(models.Model):
    
    nom = models.CharField(max_length=255)
    slug = models.SlugField()
    
    def __str__(self):
        
        return self.nom



class Produit(models.Model):
    
    categorie = models.ForeignKey(Categorie, related_name='produit', on_delete=models.CASCADE)
    
    name = models.CharField(max_length=255)
    
    price = models.IntegerField()
    
    description = models.TextField()
    
    pribarrer = models.IntegerField(default=0, null=True, blank=True)
    
    texte = models.TextField(null=True, blank=True)
    
    nom_vendeur = models.CharField(max_length=255, null=True, blank=True)
    
    prix_livraison = models.IntegerField(null=True, blank=True)
    
    logo = models.ImageField(upload_to='', null=True, blank=True)
    
    image = models.ImageField(upload_to='')
    
    
    def __str__(self):
        
        return self.name
