from django.shortcuts import render
from View.models import Exchange
from django.contrib.auth.decorators import login_required

@login_required # redirects user to login page if not logged in
def Homepage(request):
    """View function for home page of site."""
    
    RefExchange = Exchange.objects.values_list('DecimalValue', flat=True).get(ExchangeID=1) # gets the exchange rates from the exchange table
    KeyExchange = Exchange.objects.values_list('DecimalValue', flat=True).get(ExchangeID=2)
    USDExchange = Exchange.objects.values_list('DecimalValue', flat=True).get(ExchangeID=3)


    context = {
        'RefExchange': RefExchange, #puts the data into context allowing it to be accessed in the html
        'KeyExchange': KeyExchange,
        'USDExchange': USDExchange,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'Homepage.html', context=context)