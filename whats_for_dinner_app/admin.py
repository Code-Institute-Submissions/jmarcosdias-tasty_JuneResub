from django.contrib import admin
from .models import Recipe
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'author')
    search_fields = ['title', 'short_description', 'ingredients', 'method']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('short_description', 'ingredients', 'method',)
