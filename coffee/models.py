from django.db import models

# Create your models here.
class Coffee(models.Model): #automatically creates models
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2083)