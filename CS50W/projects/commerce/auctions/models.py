from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    pass

class Listing(models.Model):
    is_open = models.BooleanField(default=True)
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=100, default="")
    created_on = models.DateTimeField(auto_now_add=True)
    picture_url = models.TextField(max_length=1000)
    category = models.CharField(max_length=20)
    user_upload = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    bidding_times = models.IntegerField(default=0)
    last_bid_id = models.CharField(max_length=64, default=0)
    def __str__(self):
        return f"{self.name} has price: {self.price}, description: {self.description}, and category: {self.category} was upload by {self.user_upload}. URL img is {self.picture_url}"

class Comment(models.Model):
    text = models.CharField(max_length=200)
    user_id = models.CharField(max_length=64, default=0)
    listing_id = models.CharField(max_length=64, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text} by {self.user_id} in {self.listing_id} on {self.created_on}"

class Bid(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    user_id = models.CharField(max_length=64, default=0)
    listing_id = models.CharField(max_length=64, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: {self.price} in {self.listing_id} by {self.user_id} on {self.created_on}"
    
class UserWatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, default="")

    def __str__(self):
        return f"{self.user} is watching {self.listing}"