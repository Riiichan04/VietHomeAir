from django.db import models

from application.models.bnb_detail import Image, Category, Rule, Service


class BnbInformation(models.Model):
    name = models.CharField()
    description = models.TextField()
    address = models.TextField()
    price = models.DecimalField()
    capacity = models.IntegerField()
    count_viewed = models.IntegerField()
    # image = models.ForeignKey(Image, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    rule = models.ManyToManyField(Rule)
    service = models.ManyToManyField(Service)
