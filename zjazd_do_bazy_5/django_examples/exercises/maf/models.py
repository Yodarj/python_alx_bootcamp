from django.db import models

# Create your models here.

class Math(models.Model):
    func = models.CharField(max_length=10)
    l1 = models.FloatField()
    l2 = models.FloatField()

