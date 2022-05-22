from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.views import generic, View
from django.template.defaultfilters import slugify
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


class CreateRecipeView(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "create_recipe.html",
            {
                "recipe_form": RecipeForm()
            },
        )

    def post(self, request, *args, **kwargs):
        recipe_form = RecipeForm(data=request.POST)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.slug = slugify(recipe.title)
            recipe.save()
        else:
            recipe_form = RecipeForm()

        return render(
            request,
            "create_recipe.html",
        )
        # print("post recipe")
        # title = request.POST.get('title')
        # short_description = request.POST.get('short_description')
        # ingredients = request.POST.get('ingredients')
        # method = request.POST.get('method')
        # Recipe.objects.create(title=title, author=request.user,
        #   short_description=short_description, ingredients=ingredients, method=method)
        # print("title = " + title)
        # form = RecipeForm(request.POST)
        # if form.is_valid():
        # form.save()
        # return redirect('home')


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