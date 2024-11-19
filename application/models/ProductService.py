from django.db import models

list_img = list()
list_rules = list()

class ServiceImage:
    def __init__(self, list_url):
        self.list_url = list(list_url)

class ServiceRules:
    def __init__(self, list_rule):
        self.list_rules = list(list_rule)


class ProductService(models.Model):
    name = models.TextField()
    detail = models.TextField()
    description = models.TextField()
    place = models.TextField()
    status = models.TextField()
    price = models.IntegerField()
    time = models.DateTimeField()
    capacity = models.IntegerField()

    list_image = ServiceImage(list_img)
    list_rules = ServiceRules(list_rules)


