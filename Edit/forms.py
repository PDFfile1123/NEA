from django import forms
from View.models import Exchange

class ExchangeForm(forms.ModelForm): #creates a form inheriting from the Exchange rate model so that any information edited in the form will update the parent model
    class Meta:
        model = Exchange
        fields = ["DecimalValue"]