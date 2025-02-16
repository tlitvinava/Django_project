from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=30, unique=True)
    expiration_date = models.DateField()
    appearance = models.CharField(max_length=30)
    proteins = models.CharField(max_length=30)
    fats = models.CharField(max_length=30)
    carbohydrates = models.CharField(max_length=30)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)

class Categories(models.Model):
    name = models.CharField(max_length=30, unique=True)
    storage_methods = models.CharField(max_length=30)
    vitamins = models.CharField(max_length=30)
