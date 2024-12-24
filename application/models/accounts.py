from django.db import models
from django.forms import DecimalField, IntegerField, DateTimeField


# from application.models.bnb import BnbInformation

class Account(models.Model):
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=500)
    email = models.CharField(unique=True, max_length=200)
    phone = models.CharField(max_length=11, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    fullname = models.CharField(max_length=200)
    gender = models.CharField(max_length=6, choices=(('male', 'Male'), ('female', 'Female'), ('other', 'Other')))
    role = models.IntegerField()
    register_time = DateTimeField()
    is_verified = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    avatar = models.TextField(default='https://res.cloudinary.com/dh90ponfw/image/upload/v1725050290/default_avatar.webp')

class Owner(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    rating = DecimalField(max_digits=5, decimal_places=2)


class OwnerReview(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    sentiment = models.CharField(max_length=8,
                                 choices=(('none', None), ('positive', 'POS'), ('negative', 'NEG'), ('neutral', 'NEU')))
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    rating = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('owner', 'account')


class WishList(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='wishlist')


class WishListItems(models.Model):
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE, related_name='items')
    bnb_id = models.ForeignKey('application.BnbInformation', on_delete=models.CASCADE)
    added_time = models.DateTimeField(auto_now_add=True)


class Booking(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    bnb = models.ForeignKey('application.BnbInformation', on_delete=models.CASCADE)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    capacity = models.IntegerField()
    status = models.CharField(max_length=7,
                              choices=(('pending', 'Pending'), ('accept', 'Accept'), ('decline', 'Decline'),
                                       ('served', 'Served')))

    class Meta:
        unique_together = ('account', 'bnb', 'from_date', 'to_date')
