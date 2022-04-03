# Generated by Django 2.2 on 2021-05-23 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0004_commentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMeModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=2000, verbose_name='关于我')),
            ],
            options={
                'verbose_name_plural': '关于我',
                'db_table': 'about_me',
            },
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name_plural': '博客'},
        ),
        migrations.AlterModelOptions(
            name='commentmodel',
            options={'verbose_name_plural': '文章评论'},
        ),
        migrations.AlterModelOptions(
            name='duanzi',
            options={'managed': False, 'verbose_name_plural': '搞笑段子'},
        ),
        migrations.AlterModelOptions(
            name='leaveamessagemodel',
            options={'verbose_name_plural': '留言'},
        ),
    ]