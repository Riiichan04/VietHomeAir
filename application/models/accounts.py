from django.db import models
from django.forms import DecimalField, IntegerField, DateTimeField

from application.models.bnb import BnbInformation


class Account(models.Model):
    username = models.CharField(unique=True)
    password = models.CharField(length=32)
    email = models.CharField()
    description = models.TextField()
    fullname = models.CharField()
    gender = models.CharField(choices=(('male', 'Male'), ('female', 'Female'), ('other', 'Other')))
    role = models.IntegerField()
    register_time = DateTimeField()
    status = models.BooleanField(default=True)


class Owner(Account):
    rating = DecimalField(max_digits=5, decimal_places=2)
    count_rating = models.IntegerField(default=0)

class WishList(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='wishlist')


class WishListItems(models.Model):
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE, related_name='items')
    bnb_id = models.ForeignKey(BnbInformation, on_delete=models.CASCADE)
    added_time = models.DateTimeField(auto_now_add=True)


class Booking(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    bnb = models.ForeignKey(BnbInformation, on_delete=models.CASCADE)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    capacity = models.IntegerField()
    status = models.CharField(
        choices=(('pending', 'Pending'), ('accept', 'Accept'), ('decline', 'Decline'), ('served', 'Served')))

    class Meta:
        unique_together = ('account', 'bnb', 'from_date', 'to_date')