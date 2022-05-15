from django.shortcuts import render
from django.views import generic 
from .models import Recipe

class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter().order_by('title')
    template_name = "index.html"
    paginate_by = 6
