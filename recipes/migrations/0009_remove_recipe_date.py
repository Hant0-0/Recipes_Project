# Generated by Django 4.1.5 on 2023-02-03 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_alter_recipe_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='date',
        ),
    ]
