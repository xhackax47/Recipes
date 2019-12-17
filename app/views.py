from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.urls import reverse
from django.views import generic

from app.forms import RegisterForm, RecipeForm, IngredientForm
from app.models import Recipe, Ingredient, Tag


class IndexView(generic.TemplateView):
    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['name'] = "DjangoUser"
        result['recipes'] = Recipe.objects.all()
        result['tags'] = Tag.objects.all()
        return result

    template_name = "index.html"


class RecipeListView(generic.ListView):
    model = Recipe
    template_name = "list/recipes_list.html"


class RecipeSearchByIngredientListView(generic.ListView):
    template_name = "list/recipes_list.html"

    def get_queryset(self):
        return Recipe.objects.filter(ingredients__ingredient__name__icontains=self.kwargs['search']).distinct()


class RecipeDetailView(generic.DetailView):
    model = Recipe
    template_name = "details/recipes_detail.html"


class IngredientListView(generic.ListView):
    model = Ingredient
    template_name = "list/ingredients_list.html"


class IngredientDetailView(generic.DetailView):
    model = Ingredient
    template_name = "details/ingredients_detail.html"


class TagListView(generic.ListView):
    model = Tag
    template_name = "list/tags_list.html"


class TagDetailView(generic.DetailView):
    model = Tag
    template_name = "details/tags_detail.html"


class RecipeSearchByTagListView(generic.ListView):
    template_name = "list/tags_list.html"

    def get_queryset(self):
        return Recipe.objects.filter(tags__description__icontains=self.kwargs['search']).distinct()


class RecipeSearchByRecipeListView(generic.ListView):
    template_name = "list/recipes_list.html"

    def get_queryset(self):
        return Recipe.objects.filter(tags__recipe__description__icontains=self.kwargs['search']).distinct()


class RegisterFormView(generic.FormView):
    template_name = 'forms/register_form.html'
    form_class = RegisterForm

    def get_success_url(self):
        return reverse('register_success')

    def form_valid(self, form):
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        username_base = email.replace('@', 'at')
        try:
            User.objects.create_user(username=username_base,
                                     email=email,
                                     password=password,
                                     first_name=first_name,
                                     last_name=last_name)
        except IntegrityError:
            form.add_error('email', 'Email déjà utilisé')
            return super().form_invalid(form)

        messages.success(self.request, 'L\'utilisateur a bien été crée')
        return super().form_valid(form)


class RegisterSuccessView(generic.TemplateView):
    template_name = "registration/register_success.html"
    

class RecipeFormView(generic.FormView):
    template_name = 'forms/recipe_form.html'
    form_class = RecipeForm

    def get_success_url(self):
        return reverse('recipes_list')

    def form_valid(self, form):
        title = form.cleaned_data['title']
        description = form.cleaned_data['description']
        detail = form.cleaned_data['detail']
        tags = form.cleaned_data['tags']
        recipe = Recipe.objects.create(
            title=title,
            description=description,
            detail=detail,
        )
        recipe.tags.set(tags)
        return super().form_valid(form)


class IngredientFormView(generic.FormView):
    template_name = 'forms/ingredient_form.html'
    form_class = IngredientForm

    def get_success_url(self):
        return reverse('ingredients_list')

    def form_valid(self, form):
        recipe = form.cleaned_data['recipe']
        name = form.cleaned_data['name']
        description = form.cleaned_data['description']
        Ingredient.objects.create(
            name=name,
            description=description,
            recipe_id=recipe
        )

        return super().form_valid(form)
