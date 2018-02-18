from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect#
from .forms import *

# Create your views here.

#@csrf_protect#
def index(request):
    if request.method == "POST":
        ingredientForm = IngredientForm(request.POST)
        if ingredientForm.is_valid():
            quantity = ingredientForm.cleaned_data.get("quantity")
            measurement = ingredientForm.cleaned_data.get("measurement")
            name = ingredientForm.cleaned_data.get("name")
            Ingredient.objects.create(quantity=quantity,measurement=measurement,name=name)
            newIngredientForm = IngredientForm(request.POST or None,initial={"quantity": "123"})
            allIngredients = ingredient.objects.all()
            context = {
            "cheapestPrice": "placeholder(quantity,measurement,name)",
            "ingredientForm": newIngredientForm,
            "allIngredients": allIngredients
            }
            print("form is valid")
            return render(request, "design_2.html", context)
        else:
            print("invalid")
    else:
        ingredientForm = IngredientForm(request.POST or None)
        context = {
        "ingredientForm": IngredientForm
        }
        return render(request, "design_2.html", context)

def ingredient_new(request):
    form = IngredientForm()
    return render(request, './templates/ingredient_edit.html', {'form': form})
