
from django import forms
from . import forms, models
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from decimal import *

from .models import Listing, User
from .forms import ListingForm


# Create your views here.
def index(request):
    listings = []
    items = Listing.objects.filter()
    for item in items:
       
        listings.append({
            'listing': item,
            
        })
    context = {
        'listings': listings,
    }
    return render(request, "auction_app/index.html", context)

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auction_app/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auction_app/login.html")

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auction_app/signup.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auction_app/signup.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auction_app/signup.html")


def addListing(request):
    if request.method == "POST":
        form = ListingForm(request.POST)

        if form.is_valid():
            newListing = form.save(commit=False)
            newListing.user = request.user
            newListing.save()
            messages.success(request, 'Successfully created your listing.', fail_silently=True)
        else:
            messages.error(request, 'Invalid Listing!', fail_silently=True)
            return HttpResponseRedirect('addListing')
        return redirect(reverse("index"))
    form = ListingForm()
    context = {
        'form': form,
    }
    return render(request, 'auction_app/createauction.html', context)

def user_listings(request):
    listings = []
    current_user_listings = Listing.objects.filter(user=request.user)
    for item in current_user_listings:
        
        listings.append({
            'listing': item,
            
        })
    context = {
        'listings': Listing,
    }
    
    return render(request, 'auction_app/mylisting.html', context)
