# Generated by Django 4.1.5 on 2023-02-03 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_remove_recipe_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='date_create',
        ),
    ]
