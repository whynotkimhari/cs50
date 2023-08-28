from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    is_in_watch_list = models.BooleanField(default=False)
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=100, default="")
    created_on = models.DateTimeField(auto_now_add=True)
    picture_url = models.TextField(max_length=1000)
    category = models.CharField(max_length=20)
    user_upload = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    bidding_times = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.name} has price: {self.price}, description: {self.description}, and category: {self.category} was upload by {self.user_upload}. URL img is {self.picture_url}"

class Comment(models.Model):
    text = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

class Bid(models.Model):
    last_price = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    bidding_times = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)