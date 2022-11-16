from django.db import models

# Create your models here.

class coinStore(models.Model):
    name = models.CharField(max_length=300)
    symbol = models.CharField(max_length=300)
    price = models.CharField(max_length=300)
    change = models.CharField(max_length=300)
    volume = models.CharField(max_length=300)
    market_cap = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    time = models.DateTimeField(auto_now_add=True)
