# Generated by Django 4.2.15 on 2024-08-27 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_alter_posts_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
    ]
