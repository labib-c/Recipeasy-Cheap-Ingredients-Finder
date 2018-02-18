from .models import *
from django import forms

class IngredientForm(forms.Form):
    class Meta:
        model = Ingredient
        fields = ["name", "quantity", "measurement"]

        labels = {"name": "Name of the ingredient", "quantity": "Quantity of the ingredient", "measurement": "Unit"}
