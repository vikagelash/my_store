from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, default="user")
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f"{self.name} {self.last_name}"




