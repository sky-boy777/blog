# Generated by Django 2.2 on 2022-05-06 22:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_auto_20220503_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcommentmodel',
            name='blog',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='blog_app.BlogModel', verbose_name='评论的文章'),
        ),
        migrations.AlterField(
            model_name='blogcommentmodel',
            name='user',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='评论所属用户'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='blog_type',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='blog_app.BlogTypeModel', verbose_name='文章分类'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='user',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
    ]