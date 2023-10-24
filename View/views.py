from django.shortcuts import render
from .models import *
from .tables import ScrapeTable
from django_tables2 import SingleTableView

class View(SingleTableView):
    """View function for home page of site."""
    model = Scrape  
    table_class: ScrapeTable
    template_name = 'View.html'
    # Render the HTML template index.html with the data in the context variable