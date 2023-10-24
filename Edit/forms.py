from django import forms
from View.models import Exchange

class ExchangeForm(forms.ModelForm):
    class Meta:
        model = Exchange
        fields = ["DecimalValue"]