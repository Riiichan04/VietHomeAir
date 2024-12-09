from django.db import models

from application.models.accounts import Account
from application.models.bnb import BnbInformation

# ManyToMany -> Không cần foreign key tới BnbInformation
class Service(models.Model):
    name = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Rule(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()

# OneToMany -> Cần foreign key tới BnbInformation
class Image(models.Model):
    url = models.CharField(unique=True)
    product = models.ForeignKey(BnbInformation, on_delete=models.PROTECT)

class Review(models.Model):
    product = models.ForeignKey(BnbInformation, on_delete=models.PROTECT)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    sentiment = models.CharField(choices=(None, 'NEG', 'POS', 'NEU'))
    rating = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('product', 'account')

class BnbLocation(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()