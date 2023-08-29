from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Listing, Comment, Bid, UserWatchList
import datetime

## Display all active listings
def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.filter(
            is_open = True,
        )
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
    
## Let authenticated user create a listing
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

        ## DELETE ALL LISTING, JUST USE WHEN MAKE THIS WEBSITE
        # Listing.objects.all().delete()
    return render(request, "auctions/createlisting.html")

## Display the details of a listing, let user bid
def listing(request, id):
    listing = Listing.objects.get(id=id)
    last_bid_id = listing.last_bid_id
    user_id = request.user.id

    ## HANDLER FOR COMMENTS ORDERING
    reverse_comments = [{
            "user": User.objects.get(id=int(comment.user_id)),
            "text": comment.text,
            "created_on": comment.created_on
        } for comment in Comment.objects.filter(
            listing_id=id
        )]

    comments = []

    for i in range(len(reverse_comments) - 1, -1, -1):
        comments.append(reverse_comments[i])

    if last_bid_id != "0":
        bid = Bid.objects.get(id=last_bid_id)
    else:
        bid = None

    try:
        last_bidding = User.objects.get(id=bid.user_id)
    except AttributeError:
        last_bidding = None

    if user_id:
        try:
            watchlist = UserWatchList.objects.get(
                user=request.user, 
                listing=listing
            )
            is_in_watchlist = True
        except UserWatchList.DoesNotExist:
            is_in_watchlist = False

        return render(request, "auctions/listing.html", {
            "is_in_watchlist": is_in_watchlist,
            "last_bidding": last_bidding,
            "listing": listing,
            "user_id": user_id,
            "bid": bid,
            "comments": comments,
        })

    else:
        return render(request, "auctions/listing.html", {
            "last_bidding": last_bidding,
            "listing": listing,
            "user_id": user_id,
            "bid": bid,
            "comments": comments
        })

## Processing the bidding, the item will automatically be added to
## the watch list when bidding command is called
@login_required
def bid(request, id):
    if request.method == "POST":
        user_id = request.user.id
        bid_value = float(request.POST.get("bid_value"))
        listing = Listing.objects.get(id=id)
        
        ## HANDLER FOR COMMENTS ORDERING
        reverse_comments = [{
                "user": User.objects.get(id=int(comment.user_id)),
                "text": comment.text,
                "created_on": comment.created_on
            } for comment in Comment.objects.filter(
                listing_id=id
            )]

        comments = []

        for i in range(len(reverse_comments) - 1, -1, -1):
            comments.append(reverse_comments[i])


        if bid_value <= listing.price:
            return render(request, "auctions/listing.html", {
                "listing": listing,
                "user_id": user_id,
                "msg": f"Your bid must be greater than ${listing.price}!",
                "comments": comments
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

            UserWatchList.objects.create(
                user=request.user,
                listing=listing
            )

            return render(request, "auctions/listing.html", {
                "last_bidding": User.objects.get(id=bid.user_id),
                "listing": listing,
                "user_id": user_id,
                "bid": bid,
                "msg": "Successfully bid!",
                "comments": comments
            })
    
## Let owner of item an ability to close the biddings and 
## notify the user who bid the highest that they won
@login_required
def close(request, id):
    if request.method == "POST":
        listing = Listing.objects.get(id=id)
        listing.is_open = False
        listing.save()
        return HttpResponseRedirect(reverse("listing", kwargs={'id': id}))
    
## Let user see all listing in their watch list
## Even if that is terminated by the owner
@login_required
def watchlist(request):
    return render(request, "auctions/watchlist.html", {
        "watchlist": [wL.listing for wL in UserWatchList.objects.filter(
            user=request.user
        )]
    })

## Let user add item to their own watch list
## Or bid will also do this
@login_required
def addtowatchlist(request):
    if request.method == "POST":
        listing_id = int(request.POST.get('listing_id'))
        listing = Listing.objects.get(id=listing_id)
        user = User.objects.get(id=request.user.id)
        UserWatchList.objects.create(
            user=user,
            listing=listing
        )
        return HttpResponseRedirect(reverse("listing", kwargs={'id': listing_id}))

## Let user remove item to their own watch list  
@login_required
def removefromwatchlist(request):
    if request.method == "POST":
        listing_id = int(request.POST.get('listing_id'))
        listing = Listing.objects.get(id=listing_id)
        user = User.objects.get(id=request.user.id)
        UserWatchList.objects.get(
            user=user,
            listing=listing
        ).delete()
        return HttpResponseRedirect(reverse("listing", kwargs={'id': listing_id}))
    
## Let user see all the categories
@login_required
def categories(request):
    categories = set([listing.category for listing in Listing.objects.all()])

    return render(request, "auctions/categories.html", {
        "categories": categories
    })

## Let user see all the listings in the specified category
@login_required
def category(request, name):
    listings = Listing.objects.filter(
        category = name,
        is_open = True,
    )
    return render(request, "auctions/category.html", {
        "category": name,
        "listings": listings
    })

@login_required
def comment(request):
    if request.method == "POST":
        listing_id = request.POST.get('listing_id')
        text = request.POST.get('text')

        Comment.objects.create(
            text=text,
            user_id = request.user.id,
            listing_id = listing_id,
        )

        return HttpResponseRedirect(reverse("listing", kwargs={'id': listing_id}))
