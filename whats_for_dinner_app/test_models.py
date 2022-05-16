from django.test import TestCase
from .models import User, Recipe

class TestModels(TestCase):

    def test_str_recipe_returns_title(self):
        user = User.objects.create(username='test1');
        recipe1 = Recipe.objects.create(title="recipe 1 title", author=user, slug="recipe-1-title", short_description="recipe 1 short description", 
            ingredients="recipe 1 ingredients", method="recipe 1 method")
        self.assertEqual(str(recipe1), "recipe 1 title")

    def test_three_recipes_inserted(self):
        user = User.objects.create(username='test1');
        recipe1 = Recipe.objects.create(title="recipe 1 title", author=user, slug="recipe-1-title", short_description='recipe 1 short description', 
            ingredients="recipe 1 ingredients", method="recipe 1 method")
        recipe2 = Recipe.objects.create(title="recipe 2 title", author=user, slug="recipe-2-title", short_description='recipe 2 short description', 
            ingredients="recipe 2 ingredients", method="recipe 2 method")
        recipe3 = Recipe.objects.create(title="recipe 3 title", author=user, slug="recipe-3-title", short_description='recipe 3 short description', 
            ingredients="recipe 3 ingredients", method="recipe 3 method")
        self.assertEqual(Recipe.objects.all().count(),3)