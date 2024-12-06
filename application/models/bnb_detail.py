from django.db import models

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