from View.models import Item, Scrape, Rarity

def MarketplaceItemClean(ItemData,):
    if Item.objects.filter(Name=ItemData[0]).exists():
        pass
    else:
        if ItemData[4] == "Hat":
            Type = "hats"
        else:
            Type= ItemData[4].lower()
        ItemRecord = Item(Name=ItemData[0], Type= Type)
        
        return ItemRecord
        
def MarketplaceScrapeClean(ItemData):
 
    CurrencyID = ItemData[2]
    ExchangeID=2
    
    RarityID=Rarity.objects.values_list('RarityID', flat=True).get(Rarity=ItemData[7])
        
    try:
        ItemID=Item.objects.values_list('ItemID', flat=True).get(Name=ItemData[0])
    except:
        print(ItemData[0])
        MarketplaceItemClean(ItemData).save()
        ItemID=Item.objects.values_list('ItemID', flat=True).get(Name=ItemData[0])
        
    try:    
        ScrapeRecord= Scrape(Price= ItemData[1], Availability=int(ItemData[3]), ExchangeID_id=ExchangeID, ItemID_id=ItemID, LocationID_id=2, CurrencyID_id= CurrencyID, Transaction= ItemData[4],  RarityID_id=int(ItemData[11]), Painted=ItemData[3] )
        return ScrapeRecord
    except:
        print("Scrape Record incomplete")
        