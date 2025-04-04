from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100, default="Title")
    description = models.TextField()
    price = models.FloatField()
    release_date = models.DateTimeField()
    picture = models.ImageField(default="No Image")
