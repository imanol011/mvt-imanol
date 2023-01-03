from django.db import models

# Create your models here.

class Family(models.Model):
    name = models.CharField(max_length=80)
    age = models.FloatField()
    married = models.BooleanField()