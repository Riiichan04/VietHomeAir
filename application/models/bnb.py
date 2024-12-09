from django.db import models

from application.models.bnb_detail import Image, Category, Rule, Service, Location

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
