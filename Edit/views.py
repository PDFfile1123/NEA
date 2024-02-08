from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import ExchangeForm
from View.models import Exchange
from django.contrib.auth.decorators import login_required

@login_required
# Create your views here.
def Edit(request, pk):
    ExchangeInstance = get_object_or_404(Exchange, ExchangeID=pk) # gets the primary key from the URL and uses it to get the right row from the table

    # If this is a POST request then process the Form data
    form = ExchangeForm(request.POST or None, request.FILES or None, instance=ExchangeInstance)
     
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()

    # If this is a GET (or any other method) create the default form.

    context = {
        'form': form,
        'ExchangeInstance': ExchangeInstance,
    }

    return render(request, 'Edit.html', context)