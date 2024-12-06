from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    bnb_id = models.IntegerField()

class Image(models.Model):
    url = models.CharField(unique=True)
    bnb_id = models.IntegerField()

class Rule(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
