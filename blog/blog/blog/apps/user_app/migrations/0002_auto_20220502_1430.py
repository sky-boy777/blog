# Generated by Django 2.2 on 2022-05-02 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='是否删除'),
        ),
    ]