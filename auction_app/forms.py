from django import forms
from django.forms import ModelForm
from .models import Listing

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = ['name', 'description','minimum_bid_price', 'image','auction_end_date_time']