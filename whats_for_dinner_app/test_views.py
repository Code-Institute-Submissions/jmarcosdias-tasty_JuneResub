from django.test import TestCase
from .models import User, Recipe

class TestViews(TestCase):

    def test_get_recipe_list(self):
        user = User.objects.create(username='test1')
        # inserts three recipes
        recipe1 = Recipe.objects.create(title="recipe 1 title", author=user, 
            slug="recipe-1-title", short_description='recipe 1 short description', 
            ingredients="recipe 1 ingredients", method="recipe 1 method")
        recipe2 = Recipe.objects.create(title="recipe 2 title", author=user, 
            slug="recipe-2-title", short_description='recipe 2 short description', 
            ingredients="recipe 2 ingredients", method="recipe 2 method")
        recipe3 = Recipe.objects.create(title="recipe 3 title", author=user,
            slug="recipe-3-title", short_description='recipe 3 short description', 
            ingredients="recipe 3 ingredients", method="recipe 3 method")
        # successful response
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # templates used
        self.assertTemplateUsed(response, 'index.html')
        self.assertTemplateUsed(response, 'base.html')
        # title and short description of the inserted recipes are included
        # in the response
        self.assertContains(response, "recipe 1 title")
        self.assertContains(response, "recipe 1 short description")
        self.assertContains(response, "recipe 2 title")
        self.assertContains(response, "recipe 2 short description")
        self.assertContains(response, "recipe 3 title")
        self.assertContains(response, "recipe 3 short description")

