import django_tables2 as tables
from .models import *


class ScrapeTable(tables.Table):
    class Meta:
        model = Scrape
        template_name = "django_tables2/bootstrap.html"
        fields = ("ScrapeID", "Date", "Transaction", "price", "Availability", "ItemID_id", "RarityID_id", "Level", "Painted")
        
    