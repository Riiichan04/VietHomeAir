from django.db import models

from application.models.bnb_detail import Image, Category, Rule, Service, BnbLocation

class BnbInformation(models.Model):
    name = models.CharField()
    description = models.TextField()
    location = models.OneToOneField(BnbLocation, on_delete=models.CASCADE)
    price = models.DecimalField()
    capacity = models.IntegerField()
    count_viewed = models.IntegerField()
    category = models.ManyToManyField(Category)
    rule = models.ManyToManyField(Rule)
    service = models.ManyToManyField(Service)
