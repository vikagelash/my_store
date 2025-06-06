from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, default="user")
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=100, blank=False, default="default_password")

    def __str__(self):
        return f"{self.name} {self.last_name}"




