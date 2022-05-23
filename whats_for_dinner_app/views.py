from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.template.defaultfilters import slugify
from django.db import IntegrityError
from .models import Recipe
from .forms import RecipeForm, EditRecipeForm


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter().order_by('title')
    template_name = "index.html"
    paginate_by = 6


class RecipeView(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.order_by('title')
        recipe = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "recipe.html",
            {
                "recipe": recipe
            },
        )


class DeleteRecipeView(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.order_by('title')
        recipe = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "delete_recipe.html",
            {
                "recipe": recipe
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.order_by('title')
        recipe = get_object_or_404(queryset, slug=slug)
        recipe.delete()
        return redirect('home')


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


class EditRecipeView(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.order_by('title')
        recipe = get_object_or_404(queryset, slug=slug)
        return render(
            request,
            "edit_recipe.html",
            {
                "recipe": recipe,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.order_by('title')
        recipe = get_object_or_404(queryset, slug=slug)
        recipe.title = request.POST['title']
        recipe.slug = slugify(recipe.title)
        recipe.short_description = request.POST['short_description']
        recipe.ingredients = request.POST['ingredients']
        recipe.method = request.POST['method']
        try:
            recipe.save()
        except IntegrityError:
            message_to_user = "There is another recipe with this same " \
                + "title. Please try a different title."
        except Exception:
            message_to_user = "Something went wrong. Please try again."
            return render(
                request,
                "edit_recipe.html",
                {
                    "recipe": recipe,
                    "message_to_user": message_to_user,
                },
            )
        else:
            message_to_user = "Your recipe is saved."

        return render(
            request,
            "edit_recipe.html",
            {
                "recipe": recipe,
                "message_to_user": message_to_user
            },
        )
