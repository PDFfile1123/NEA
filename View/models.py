from django.db import models
from django.urls import reverse
# Create your models here.

class Item(models.Model):
    ItemID= models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Type = models.CharField(max_length=20)
    Equip =  models.CharField(max_length=20, default="")
    Class =  models.CharField(max_length=100, default="")
    def __str__(self):
        return self.Name
    
class Rarity(models.Model):
    RarityID= models.AutoField(primary_key=True)
    Rarity = models.CharField(max_length=20)
    def __str__(self):
        return self.Rarity   

class Location(models.Model):
    LocationID= models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    URL = models.URLField(max_length=100)
    def __str__(self):
        return self.Name    
    
class Exchange(models.Model):
    ExchangeID= models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    DecimalValue = models.DecimalField(decimal_places=2, max_digits=20)
    def __str__(self):
        return self.Name  
    
class Currency (models.Model):
    CurrencyID= models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    def __str__(self):
        return self.Name 
    
class Scrape(models.Model):
    ScrapeID= models.AutoField(primary_key=True)
    Date = models.DateField(auto_now=True)
    Price = models.DecimalField(decimal_places=2, max_digits=20,default=0.00)
    Availability = models.IntegerField()
    Transaction = models.CharField(max_length=10)# checks whether it is a buy order or sell order
    Level = models.CharField(max_length=10, default="")
    LocationID = models.ForeignKey(Location, on_delete=models.CASCADE)
    ExchangeID = models.ForeignKey(Exchange, on_delete=models.CASCADE)
    RarityID = models.ForeignKey(Rarity, on_delete=models.CASCADE)
    ItemID = models.ForeignKey(Item, on_delete=models.CASCADE)
    CurrencyID = models.ForeignKey(Currency, on_delete=models.CASCADE, default="")
    Painted = models.BooleanField(default=False)
    def __str__(self):
        return self.ScrapeID