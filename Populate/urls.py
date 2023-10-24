from django.urls import path
from . import views

urlpatterns = [
    path('', views.Populate, name='Populate'),
    path('Scrap', views.Scrap, name='Scrap'),
    path('Marketplace', views.Marketplace, name='Marketplace'),
    path('Scrap/Scrape/<str:page>', views.ScrapScrape, name='ScrapScrape'),
    path('Marketplace/Rarity/<str:Type>', views.MarketType, name='Type'), 
    path('Marketplace/Type/<str:Rarity>', views.MarketRarity, name='Rarity'), 
    path('Marketplace/Scrape', views.MarketplaceScrape, name='MarketplaceScrape'), 
]