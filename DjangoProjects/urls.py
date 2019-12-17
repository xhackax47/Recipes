"""DjangoProjects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name

from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include

from app.views import IndexView, RecipeListView, RecipeDetailView, RecipeSearchByIngredientListView, \
    IngredientDetailView, IngredientListView, TagListView, TagDetailView, RecipeSearchByTagListView, \
    RecipeSearchByRecipeListView, RegisterFormView, RecipeFormView, IngredientFormView, RegisterSuccessView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('recipes/<int:pk>', RecipeDetailView.as_view(), name="recipes_detail"),
    path('recipes/', RecipeListView.as_view(), name="recipes_list"),
    path('recipe/add', RecipeFormView.as_view(), name="recipe_form"),
    path('ingredients/<int:pk>', IngredientDetailView.as_view(), name="ingredients_detail"),
    path('ingredients/', IngredientListView.as_view(), name="ingredients_list"),
    path('ingredients/add', IngredientFormView.as_view(), name="ingredients_form"),
    path('tags/<int:pk>', TagDetailView.as_view(), name="tags_detail"),
    path('tags/', TagListView.as_view(), name="tags_list"),
    path('recipes/search-by-tags/<str:search>', RecipeSearchByTagListView.as_view(),
         name="recipes_search_by_tag_list"),
    path('recipes/search-by-ingredient/<str:search>', RecipeSearchByIngredientListView.as_view(),
         name="recipes_search_by_ingredient_list"),
    path('recipes/search-by-recipe/<str:search>', RecipeSearchByRecipeListView.as_view(),
         name="recipes_search_by_recipe_list"),
    path('', IndexView.as_view(), name="index"),
    path('register/', RegisterFormView.as_view(), name="register_form"),
    path('register_success/', RegisterSuccessView.as_view(), name="register_success"),
]

urlpatterns += i18n_patterns(
    path('accounts/', include('django.contrib.auth.urls')),
    path('recipes/<int:pk>', RecipeDetailView.as_view(), name="recipes_detail"),
    path('recipes/', RecipeListView.as_view(), name="recipes_list"),
    path('recipe/add', RecipeFormView.as_view(), name="recipe_form"),
    path('ingredients/<int:pk>', IngredientDetailView.as_view(), name="ingredients_detail"),
    path('ingredients/', IngredientListView.as_view(), name="ingredients_list"),
    path('ingredients/add', IngredientFormView.as_view(), name="ingredients_form"),
    path('tags/<int:pk>', TagDetailView.as_view(), name="tags_detail"),
    path('tags/', TagListView.as_view(), name="tags_list"),
    path('recipes/search-by-tags/<str:search>', RecipeSearchByTagListView.as_view(),
         name="recipes_search_by_tag_list"),
    path('recipes/search-by-ingredient/<str:search>', RecipeSearchByIngredientListView.as_view(),
         name="recipes_search_by_ingredient_list"),
    path('recipes/search-by-recipe/<str:search>', RecipeSearchByRecipeListView.as_view(),
         name="recipes_search_by_recipe_list"),
    path('', IndexView.as_view(), name="index"),
    path('register/', RegisterFormView.as_view(), name="register_form"),
)
