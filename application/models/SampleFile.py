from django.db import models

class HelloModel(models.Model):
    name = models.CharField(max_length=100) #Ví dụ