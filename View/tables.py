import django_tables2 as tables
from .models import *


class ScrapeTable(tables.Table): #table used by django_tables2 to create a table in html automatically
    class Meta:
        model = Scrape
        template_name = "django_tables2/bootstrap.html"
        fields = ("ScrapeID", "Date", "Transaction", "price", "Availability", "ItemID_id", "RarityID_id", "Level", "Painted")
        
    