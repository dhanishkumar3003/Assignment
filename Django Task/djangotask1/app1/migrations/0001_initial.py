# Generated by Django 4.2.15 on 2024-08-19 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('image', models.URLField(max_length=500)),
                ('posted_at', models.DateTimeField()),
                ('posted_by', models.CharField(max_length=500)),
            ],
        ),
    ]
