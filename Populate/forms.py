from django import forms

RarityTuple = [(0,"Unique"), (1, "Strange"), (2, "Vintage"), (3, "Genuine")]

TypeTuple = [( 0, "Hat"), (1, "Weapon"), (2, "Taunt"), (3, "Tool"), (4, "Ticket"), (5, "Strange Part")]

class MarketplaceParameterForm(forms.Form):
    
    Rarity = forms.ChoiceField(
        choices=RarityTuple,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    Type= forms.ChoiceField(
        choices=TypeTuple,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    