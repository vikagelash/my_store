from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, default="Title")
    description = models.TextField()
    price = models.FloatField()
    picture = models.ImageField(upload_to='product/', blank=True, null=True)

