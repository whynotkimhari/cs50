from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Listing, Comment, Bid
import datetime

def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all()
    })


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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
    
@login_required
def createlisting(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        try:
            price = float(request.POST.get('price'))
        except ValueError:
            price = 0
        url = request.POST.get('url')
        category = request.POST.get('category')
        listing = Listing(
            name=title, 
            price=price,
            description=description,
            created_on = datetime.datetime.now(),
            picture_url=url,
            category=category,
            user_upload = User.objects.get(id=request.user.id)
        )
        listing.save()

        ## DELETE
        # Listing.objects.all().delete()
    return render(request, "auctions/createlisting.html")

def listing(request, id):
    listing = Listing.objects.get(id=id)
    last_bid_id = listing.last_bid_id
    user_id = request.user.id

    if last_bid_id != "0":
        bid = Bid.objects.get(id=last_bid_id)
    else:
        bid = None

    try:
        last_bidding = User.objects.get(id=bid.user_id)
    except AttributeError:
        last_bidding = None

    return render(request, "auctions/listing.html", {
        "last_bidding": last_bidding,
        "listing": listing,
        "user_id": user_id,
        "bid": bid
    })

@login_required
def bid(request, id):
    if request.method == "POST":
        user_id = request.user.id
        bid_value = float(request.POST.get("bid_value"))
        listing = Listing.objects.get(id=id)

        if bid_value <= listing.price:
            return render(request, "auctions/listing.html", {
                "listing": listing,
                "user_id": user_id,
                "msg": f"Your bid must be greater than ${listing.price}!"
            })
        
        else:
            bid = Bid(
                price = bid_value,
                user_id = user_id,
                listing_id = id
            )
            bid.save()

            listing.bidding_times += 1
            listing.price = bid.price
            listing.last_bid_id = bid.id
            listing.save()

            return render(request, "auctions/listing.html", {
                "last_bidding": User.objects.get(id=bid.user_id),
                "listing": listing,
                "user_id": user_id,
                "bid": bid,
                "msg": "Successfully bid!"
            })
    
@login_required
def close(request, id):
    if request.method == "POST":
        listing = Listing.objects.get(id=id)
        listing.is_open = False
        listing.save()
        return HttpResponseRedirect(reverse("listing", kwargs={'id': id}))
    