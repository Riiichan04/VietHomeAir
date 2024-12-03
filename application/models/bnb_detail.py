from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Image(models.Model):
    url = models.CharField(unique=True)

class Rule(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()

class BnBDetail(models.Model):
    name = models.CharField()
    description = models.TextField()
    address = models.TextField()
    price = models.DecimalField()
    capacity = models.IntegerField()
    count_viewed = models.IntegerField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    rule = models.ManyToManyField(Rule)
    service = models.ManyToManyField(Service)
