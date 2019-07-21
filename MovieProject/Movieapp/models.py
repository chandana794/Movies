from django.db import models

class Movies(models.Model):
    Release =models.IntegerField()
    MovieNmae=models.CharField(max_length=100)
    Hero=models.CharField(max_length=100)
    Heroine=models.CharField(max_length=100)
    Rating=models.FloatField()
