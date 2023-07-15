from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=120)
    email = models.CharField(max_length=256)
    phoneno =  models.CharField(max_length=12)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin = models.CharField(max_length=10)
    desc = models.TextField()
    createdAt = models.TimeField()

    def __str__(self):
        return self.name