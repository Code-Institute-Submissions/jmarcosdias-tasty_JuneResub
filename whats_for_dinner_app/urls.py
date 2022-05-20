from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('<slug:slug>/', views.RecipeView.as_view(), name='recipe'),
    path('delete/<slug:slug>/', views.DeleteRecipeView.as_view(), name='delete_recipe'),
]