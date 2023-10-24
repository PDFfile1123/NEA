import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from urllib.parse import urlparse
import os
import time
import io
import re

Marketplace ="https://marketplace.tf/browse/tf2?"



class MarketplaceScraper():
    
    def __init__(self, OrderType, ItemType, Location, Rarity):
        
        RarityDict = {
            "Genuine": "1",
            "Vintage": "3",
            "Unique": "6",
            "Strange": "11"
        }
        
        self.OrderType = OrderType
        self.ItemType = ItemType
        self.Rarity = Rarity
        
        self.url = Location + "squality=" + RarityDict[Rarity] + "&stype=" + ItemType   
        print (self.url)

    def find_item_details(self):
        #these are used to setup how chromedriver functions
        options = webdriver.ChromeOptions()
        #options.add_argument('--headless')
        options.add_argument("user-data-dir="r"C:\Users\vleckj\AppData\Local\Google\Chrome\User Data")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')

        #this is the path to where you downloaded the chromedriver
        DRIVER_PATH= r"c:\Users\vleckj\OneDrive - Wellington College\Documents\Python\chromedriver.exe"
        driver = webdriver.Chrome(service=Service(DRIVER_PATH), options=options)

        ItemsData = [] 
        print("[INFO] beginning item collation")
        
        #this opens the webpage
        driver.get(self.url)
        
        time.sleep(30)
        
        #this finds the item list
        #ItemContainer = driver.find_element(By.ID, 'all-items')
        #print(ItemContainer)
        ItemList = driver.find_elements(By.CLASS_NAME, 'item-box appid-440')
        print(ItemList)
        for item in ItemList:
            print(item)
            NameDiv = item.find_element(By.CLASS_NAME, 'inner-name')
            
            if self.Rarity == "Unique" or self.Rarity == "Strange":
                ItemName = NameDiv.get_attribute('innerText')
            else:
                ItemText = NameDiv.get_attribute('innerText')
                RarityText = self.Rarity
                ItemName = ItemText.replace(RarityText, "")
                
            AvailabilityDiv = item.find_element(By.CLASS_NAME, 'item-box-amt decorator')
            Availability = int(str(AvailabilityDiv.get_attribute('innerText'))[:-1])
            
            PriceDiv = item.find_element(By.CLASS_NAME, 'item-box-amt decorator')
            Price = float(PriceDiv.get_attribute('innerText')[:1])
                
            
            ItemData = (ItemName, Price, 3, Availability, self.OrderType, self.ItemType, "Marketplace.tf", self.Rarity)
            print (ItemData)
            ItemsData.append(ItemData)
        
        return ItemsData 