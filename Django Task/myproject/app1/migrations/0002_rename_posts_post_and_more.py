# Generated by Django 4.2.15 on 2024-08-20 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='descriptions',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='images',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='posted_at',
            new_name='posted_ats',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='posted_by',
            new_name='posted_bys',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='titles',
        ),
    ]
