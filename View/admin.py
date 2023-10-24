from django.contrib import admin
from .models import Scrape, Location, Exchange, Rarity, Item, Currency

# Register your models here.
admin.site.register(Scrape)
admin.site.register(Location)
admin.site.register(Exchange)
admin.site.register(Rarity)
admin.site.register(Item)
admin.site.register(Currency)