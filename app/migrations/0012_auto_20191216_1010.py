# Generated by Django 3.1 on 2019-12-16 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20191216_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipetag',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.Recipe'),
        ),
    ]