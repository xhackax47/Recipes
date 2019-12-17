# Generated by Django 3.1 on 2019-12-16 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Recipe')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(through='app.RecipeTag', to='app.Tag'),
        ),
    ]