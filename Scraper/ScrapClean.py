from View.models import Item, Scrape, Exchange, Currency

def AssignType(ItemData):
    CategoryTypeDict = {
        "category-0": "tool",
        "category-1": "weapon",
        "category-2": "weapon",
        "category-3": "australium",
        "category-4": "hats",
        "category-5": "taunt",
        "category-6": "strange part",
        "category-7": "crate",
        "category-8": "key",
        "category-9": "ticket",
    }

    if ItemData[9] == 'items':
        Type = CategoryTypeDict[ItemData[12]]
    else:
        Type = ItemData[9]
    return Type

def ScrapItemClean(ItemData,):
    if Item.objects.filter(Name=ItemData[0]).exists():
        pass
    else:
        ItemRecord = Item(Name=ItemData[0], Equip= ItemData[1], Class= ItemData[2], Type= AssignType(ItemData))
        return ItemRecord
        
def ScrapScrapeClean(ItemData):
 
    if ItemData[5] == "Refined"or ItemData[5]== "Keys":
        Price = float(ItemData[4][0])    
        CurrencyID = Currency.objects.values_list('CurrencyID', flat=True).get(Name=ItemData[5])
        CurrencyName = ItemData[5]
    else:
        Price = float(ItemData[4][0]) + (float(ItemData[4][1])/64.66)
        CurrencyName = "Keys"
        CurrencyID = 2
    try:
        ExchangeID=Exchange.objects.values_list('ExchangeID', flat=True).get(Name=CurrencyName)
    except:
        print(ItemData[5])
        
    try:
        ItemID=Item.objects.values_list('ItemID', flat=True).get(Name=ItemData[0])
    except:
        print(ItemData[0])
        Item(Name=ItemData[0], Equip= ItemData[1], Class= ItemData[2], Type= AssignType(ItemData)).save()
        ItemID=Item.objects.values_list('ItemID', flat=True).get(Name=ItemData[0])
        
    try:    
        ScrapeRecord= Scrape(Price= Price, Availability=int(ItemData[6]), ExchangeID_id=ExchangeID, ItemID_id=ItemID, LocationID_id=1, CurrencyID_id= CurrencyID, Transaction= ItemData[8], Level= ItemData[7], RarityID_id=int(ItemData[11]), Painted=ItemData[3] )
        return ScrapeRecord
    except:
        print("Scrape Record incomplete")
        