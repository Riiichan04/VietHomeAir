from django.db import models
from django.forms import DecimalField, IntegerField, DateTimeField

from application.models.bnb_detail import BnBDetail


class WishList(models.Model):
    bnb_id = IntegerField()
    added_time = DateTimeField()

class Account(models.Model):
    username = models.CharField(unique=True)
    password = models.CharField(length=32)
    email = models.CharField()
    description = models.TextField()
    fullname = models.CharField()
    gender = models.CharField(choices=(('male', 'Male'), ('female', 'Female'), ('other', 'Other')))
    role = models.IntegerField()
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE)

class Owner(Account):
    rating = DecimalField(max_digits=5, decimal_places=2)
    count_rating = models.IntegerField(default=0)
    bnb_owner = models.ForeignKey(BnBDetail, on_delete=models.CASCADE)

