from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Math(models.Model):
    func = models.CharField(max_length=10)
    l1 = models.FloatField()
    l2 = models.FloatField()
    user = models.ForeignKey(User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
        )

    def __str__(self):
        return (f'Maf func: {self.func}, arguments: {self.l1}, {self.l2} ')


