from django.db import models

# Create your models here.

measurementChoices = (
                        ("kg","kg"),
                        ("pound", "pound"),
                        ("ml","ml")
                     )

class Recipe(models.Model):
    name = models.CharField(max_length=100)

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=4,decimal_places=2)
    measurement = models.CharField(max_length=100, choices = measurementChoices)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
