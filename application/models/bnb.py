from django.db import models

from application.models import Account, Owner


# ManyToMany -> Không cần foreign key tới BnbInformation
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)


class Service(models.Model):
    name = models.CharField(max_length=200, unique=True)


class Rule(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()


class Location(models.Model):
    name = models.CharField(max_length=200)
    lat = models.FloatField()
    lon = models.FloatField()


class BnbInformation(models.Model):
    name = models.CharField(max_length=300, unique=True)
    description = models.TextField()
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()
    count_viewed = models.IntegerField(default=0)
    category = models.ManyToManyField(Category)
    rule = models.ManyToManyField(Rule)
    service = models.ManyToManyField(Service)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

# OneToMany -> Cần foreign key tới BnbInformation
class Image(models.Model):
    url = models.TextField(unique=True)
    product = models.ForeignKey(BnbInformation, on_delete=models.CASCADE)


class Review(models.Model):
    bnb = models.ForeignKey(BnbInformation, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    sentiment = models.CharField(max_length=8,
                                 choices=(('none', None), ('positive', 'POS'), ('negative', 'NEG'), ('neutral', 'NEU')))
    rating = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('bnb', 'account')

class ReviewClassification(models.Model):
    review = models.OneToOneField(Review, on_delete=models.CASCADE)
    spam_status = models.BooleanField()