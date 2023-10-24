from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from View.models import Item, Scrape
from .forms import MarketplaceParameterForm
from.models import MarketplaceParameterModel
from django.shortcuts import get_object_or_404

from Scraper.ScrapScraper import ScrapScraper
from Scraper.ScrapClean import ScrapItemClean, ScrapScrapeClean

from Scraper.MarketplaceScraper import MarketplaceScraper
from Scraper.MarketplaceClean import MarketplaceItemClean, MarketplaceScrapeClean

# Create your views here.
@login_required
def Populate(request):
    return render(request, 'Populate.html')

@login_required
def Scrap(request):
    return render(request, 'Scrap.html')

@login_required
def Marketplace(request):
        
    Rarity = request.session.get('Rarity', "Unique")
    Type = request.session.get('Type', "Hat")
    context =  {
        "Rarity": Rarity,
        "Type": Type,
    }
    return render(request, 'Marketplace.html', context = context)

def MarketType(request, Type):
    request.session['Type'] = Type
    Rarity = request.session.get('Rarity')
    context =  {
        "Rarity": Rarity,
        "Type": Type,
    }
    return render(request, 'Marketplace.html', context = context)

def MarketRarity(request, Rarity):
    
    request.session['Rarity'] = Rarity
    Type = request.session.get('Type')
    
    context =  {
        "Rarity": Rarity,
        "Type": Type,
    }
    return render(request, 'Marketplace.html', context = context)



@login_required
def ScrapScrape(request, page):
    Scraper = ScrapScraper("buy", page, "https://scrap.tf/")
    ItemsData = Scraper.find_item_details()#creates a list of scraped information
    
    ItemRecordList = []
    for ItemData in ItemsData:
        try:
            ItemRecordList.append(ScrapItemClean(ItemData))
        except:
            print("item already saved")
    try:
        Item.objects.bulk_create(ItemRecordList)
    except:
        print("No new items")
        
    ScrapeRecordList = []
    for ItemData in ItemsData:
        ScrapeRecordList.append(ScrapScrapeClean(ItemData))
    Scrape.objects.bulk_create(ScrapeRecordList)
    return render(request, 'Scrap.html')
        
@login_required
def MarketplaceScrape(request):
    
    Scraper = MarketplaceScraper("buy", request.session.get('Type'), "https://marketplace.tf/browse/tf2?", request.session.get('Rarity'))
    ItemsData = Scraper.find_item_details()#creates a list of scraped information
    
    ItemRecordList = []
    for ItemData in ItemsData:
        try:
            ItemRecordList.append(MarketplaceItemClean(ItemData))
        except:
            print("item already saved")
    try:
        Item.objects.bulk_create(ItemRecordList)
    except:
        print("No new items")
        
    ScrapeRecordList = []
    for ItemData in ItemsData:
        ScrapeRecordList.append(MarketplaceScrapeClean(ItemData))
    Scrape.objects.bulk_create(ScrapeRecordList)
    return render(request, 'Scrape.html')
