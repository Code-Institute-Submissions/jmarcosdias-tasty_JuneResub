from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.views import generic, View 
from .models import Recipe
from .forms import RecipeForm

class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter().order_by('title')
    template_name = "index.html"
    paginate_by = 6

class RecipeView(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.order_by('title')
        recipe = get_object_or_404(queryset, slug=slug)
        # says wether the logged-in user is the owner of this recipe
        if recipe.author == self.request.user:
            owner = True
        else:
            owner = False
        
        return render(
            request,
            "recipe.html",
            {
                "recipe": recipe,
                "owner": owner
            },
        )

class DeleteRecipeView(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.order_by('title')
        recipe = get_object_or_404(queryset, slug=slug)
        # says wether the logged-in user is the owner of this recipe
        if recipe.author == self.request.user:
            owner = True
        else:
            owner = False
        
        return render(
            request,
            "delete_recipe.html",
            {
                "recipe": recipe,
                "owner": owner
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.order_by('title')
        recipe = get_object_or_404(queryset, slug=slug)
        recipe.delete()
        return redirect('home');


class CreateRecipeView(generic.ListView):
    model = Recipe
    template_name = "create_recipe.html"


class EditRecipeView(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.order_by('title')
        recipe = get_object_or_404(queryset, slug=slug)
        # says wether the logged-in user is the owner of this recipe
        if recipe.author == self.request.user:
            owner = True
        else:
            owner = False
        
        return render(
            request,
            "delete_recipe.html",
            {
                "recipe": recipe,
                "owner": owner
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.order_by('title')
        recipe = get_object_or_404(queryset, slug=slug)
        recipe.delete()
        return redirect('home');