from django.db import models

from application.models.accounts import Owner, Account


# ManyToMany -> Không cần foreign key tới BnbInformation
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Service(models.Model):
    name = models.CharField(max_length=100)


class Rule(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()


class BnbInformation(models.Model):
    name = models.CharField()
    description = models.TextField()
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    price = models.DecimalField()
    capacity = models.IntegerField()
    count_viewed = models.IntegerField()
    category = models.ManyToManyField(Category)
    rule = models.ManyToManyField(Rule)
    service = models.ManyToManyField(Service)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)


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
