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
        recipe = Recipe()
        recipe.title = request.POST['title']
        recipe.slug = slugify(recipe.title)
        recipe.short_description = request.POST['short_description']
        recipe.ingredients = request.POST['ingredients']
        recipe.method = request.POST['method']
        # Used by the view to allow or disallow the create button
        btn_create_disallowed = False

        if not recipe.slug:
            message_to_user = "Please provide a title for your recipe."
        else:
            recipe_form = RecipeForm(data=request.POST)
            if recipe_form.is_valid():
                recipe.author = request.user
                try:
                    recipe.save()
                except IntegrityError:
                    message_to_user = "There is another recipe with this " \
                        + "same title. Please try a different title."
                except Exception:
                    message_to_user = "Something went wrong. Please try again."
                else:
                    message_to_user = "Your recipe is saved."
                    btn_create_disallowed = True
            else:
                message_to_user = "Something went wrong. Please try again."

        return render(
            request,
            "create_recipe.html",
            {
                "recipe": recipe,
                "message_to_user": message_to_user,
                "btn_create_disallowed": btn_create_disallowed
            },
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
        # Used by the view to allow or disallow the save button
        btn_save_disallowed = False

        if not recipe.slug:
            message_to_user = "Please provide a title for your recipe."
        else:
            try:
                recipe.save()
            except IntegrityError:
                message_to_user = "There is another recipe with this same " \
                    + "title. Please try a different title."
            except Exception:
                message_to_user = "Something went wrong. Please try again."
            else:
                message_to_user = "Your recipe is saved."
                btn_save_disallowed = True

        return render(
            request,
            "edit_recipe.html",
            {
                "recipe": recipe,
                "message_to_user": message_to_user,
                "btn_save_disallowed": btn_save_disallowed
            },
        )
