# Generated by Django 3.1a1 on 2020-05-28 14:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('landing', '0013_auto_20200527_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='houses',
            name='favourites',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]