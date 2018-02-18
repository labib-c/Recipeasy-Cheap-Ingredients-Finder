from .models import *
from django import forms

class IngredientForm(forms.ModelForm):


    class Meta:
        model = Ingredient
        fields = ["quantity", "measurement", "name"]

        labels = {"quantity": "Quantity of the ingredient", "measurement": "Unit", "name": "Name of the ingredient",}
