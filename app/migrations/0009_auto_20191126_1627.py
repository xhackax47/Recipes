# Generated by Django 3.1 on 2019-11-26 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_unit_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredientunit',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='app.Recipe'),
        ),
    ]
