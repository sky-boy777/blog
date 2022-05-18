# Generated by Django 2.2 on 2022-05-08 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviemodel',
            name='IMDb_score',
            field=models.DecimalField(decimal_places=1, default=-1, max_digits=2, verbose_name='IMDb评分'),
        ),
        migrations.AddField(
            model_name='moviemodel',
            name='douban_score',
            field=models.DecimalField(decimal_places=1, default=-1, max_digits=2, verbose_name='豆瓣评分'),
        ),
    ]