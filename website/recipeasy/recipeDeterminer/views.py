from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

# Create your views here.


def index(request):
    if request.method == "POST":
        ingredientForm = IngredientForm(request.POST)
        if ingredientForm.is_valid():
            print("form is valid")
        else:
            print("invalid")
    else:
        ingredientForm = IngredientForm(request.POST or None)
        context = {
        "ingredientForm": IngredientForm
        }
        return render(request, "design_1.html", context)
