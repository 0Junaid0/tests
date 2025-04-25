from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0.00)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.name}, {self.price}"