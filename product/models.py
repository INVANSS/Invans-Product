from django.db import models

# Create your models here.
class Product(models.Model):
    rf = models.CharField(max_length=20, null=True)
    name = models.CharField(max_length=100)
    cajas = models.IntegerField(default=0)
    unidades = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.rf + "-" + self.name