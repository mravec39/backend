from django.db import models


# Create your models here.
class CPU(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    cores = models.IntegerField()
    threads = models.IntegerField()
    base_clock = models.FloatField()
    boost_clock = models.FloatField()
    cache = models.CharField(max_length=255)
    socket = models.CharField(max_length=50)
    power_draw = models.FloatField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
