from django import forms
from django.forms import widgets

from app.models import Tag, Recipe


class RegisterForm(forms.Form):
    first_name = forms.CharField(label="Prénom", max_length=200,
                                 widget=widgets.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Nom", max_length=200,
                                widget=widgets.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Adresse mail", max_length=200,
                             widget=widgets.EmailInput(attrs={'class': 'form-control'}),
                             required=True)
    password = forms.CharField(label="Mot de passe", max_length=200,
                               widget=widgets.PasswordInput(attrs={'class': 'form-control'}),
                               required=True)
    confirm_password = forms.CharField(label="Confirmer le mot de passe", max_length=200,
                                       widget=widgets.PasswordInput(attrs={'class': 'form-control'}),
                                       required=True)

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 12:
            self.add_error('password', 'La longueur minimale du mot de passe doit être de 12 caractères')
        return password

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            self.add_error('confirm_password', 'Les mots de passe doivent correspondre')
        return super().clean()


class RecipeForm(forms.Form):
    title = forms.CharField(label="Nom de la recette", min_length=5,
                            widget=widgets.TextInput(attrs={'class': 'form-control'}),
                            required=True)
    description = forms.CharField(label="Description", max_length=1000,
                                  widget=widgets.TextInput(attrs={'class': 'form-control'}))
    detail = forms.CharField(label="Détails", widget=widgets.TextInput(attrs={'class': 'form-control'}))

    choices = [(tag.pk, tag.description) for tag in Tag.objects.all()]
    tags = forms.ChoiceField(label="Mot-clé", choices=choices)


class IngredientForm(forms.Form):
    choices = [(recipe.pk, recipe.title) for recipe in Recipe.objects.all()]
    recipe = forms.ChoiceField(label="Recette", choices=choices)
    name = forms.CharField(label="Nom de l'ingrédient", max_length=200,
                           widget=widgets.TextInput(attrs={'class': 'form-control'}),
                           required=True)
    description = forms.CharField(label="Description de l'ingrédient",
                                  widget=widgets.TextInput(attrs={'class': 'form-control'}))
