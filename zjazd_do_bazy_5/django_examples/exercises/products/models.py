from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=30)
    info = models.CharField(max_length=155)
    price = models.FloatField()
    status = models.CharField(max_length=30)