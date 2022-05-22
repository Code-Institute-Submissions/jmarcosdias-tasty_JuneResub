from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    prepopulated_fields = {'slug': ('title',)}
    class Meta:
        model = Recipe
        fields = ('title', 'short_description', 'ingredients', 'method',)

