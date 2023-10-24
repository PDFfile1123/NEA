from django.db import models

# Create your models here.
class MarketplaceParameterModel(models.Model):
    Rarity = models.CharField(max_length=20,)
    Type = models.CharField(max_length=20,)