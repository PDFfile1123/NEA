import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from urllib.parse import urlparse
import os
import time
import io
import re

Scrap ="https://scrap.tf/"

class ScrapScraper():
    
    def __init__(self, OrderType, ItemType, Location):
        
        self.OrderType = OrderType
        self.ItemType = ItemType
        
        self.url = Location + OrderType+"/" + ItemType+"/"        
        print (self.url)

    def find_item_details(self):
        #these are used to setup how chromedriver functions
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        options.add_argument("user-data-dir="r"C:\Users\vleckj\AppData\Local\Google\Chrome\User Data")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')

        #this is the path to where you downloaded the chromedriver, make sure you get the right chromedriver for your version of chrome
        DRIVER_PATH= r"c:\Users\vleckj\OneDrive - Wellington College\Documents\Python\chromedriver.exe"
        driver = webdriver.Chrome(service=Service(DRIVER_PATH), options=options)

        #regexes for parsing misc data
        #PaintRegEx = r"Painted"
        PriceRefTextRegEx = r"Costs.*refined"
        PriceKeyTextRegEx = r"Costs.*key"

        PriceRegEx = r"\d+.?\d*"
        LevelRegEx = r"Level \d+"
        RarityRegEx = r"quality\d+"
        ItemNameRegEx= r">.*<"
        ItemsData = []
        
        #dictionary used to convert rarity identifier of scrap.tf into text
        RarityDict = {
            "quality1": 3,#Genuine
            "quality3": 4,#vintage
            "quality6": 1,#unique
            "quality11": 2,#strange
        }
        
        print("[INFO] beginning item collation")
        
        #this opens the webpage
        driver.get(self.url)
        
        time.sleep(3)
        
        #this finds the item list
        BankingCategories = driver.find_elements(By.CLASS_NAME, 'banking-category')
        for BankingCategory in BankingCategories:
            CategoryName = BankingCategory.get_attribute('id')
            ItemContainer= BankingCategory.find_element(By.CLASS_NAME, 'items-container')
            ItemList= ItemContainer.find_elements(By.XPATH, './div')
        
            for item in ItemList:
                RarityData=item.get_attribute('class')
                RarityText = re.search(RarityRegEx, RarityData).group()
                Rarity = RarityDict[RarityText]
                
                EquipRegion=item.get_attribute('data-slot')
                EquipMerc=item.get_attribute('data-classes')
                ContentData = item.get_attribute('data-content')
                
                if Rarity == 3 or Rarity == 1:
                    ItemName = item.get_attribute('data-title')
                else:
                    ItemText = item.get_attribute('data-title')
                    ItemName = str(re.search(ItemNameRegEx, ItemText).group()).strip("><")
                Availability = int(item.get_attribute('data-num-available'))
                
                Level = re.search(LevelRegEx, ContentData).group()
                
                Paint = "Painted" in ContentData
                
                try:
                    PriceText = re.search(PriceRefTextRegEx, ContentData).group()
                    price =re.findall(PriceRegEx, PriceText)
                    if len(price) == 1:
                        Currency = "Refined"
                    else:         
                        Currency = 5
                except:
                    PriceText = re.search(PriceKeyTextRegEx, ContentData).group()
                    price =re.findall(PriceRegEx, PriceText)
                    Currency = "Keys"
                    
                
                ItemData = (ItemName, EquipRegion, EquipMerc, Paint, price, Currency, Availability, Level, self.OrderType, self.ItemType, "Scrap.tf", Rarity, CategoryName)
                print (ItemData)
                ItemsData.append(ItemData)
        
        return ItemsData  
    
            
    




