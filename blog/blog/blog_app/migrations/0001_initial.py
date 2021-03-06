# Generated by Django 2.2 on 2020-08-03 17:21

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Duanzi',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField(blank=True, null=True, verbose_name='段子')),
                ('favour', models.IntegerField(default=0, null=True, verbose_name='获赞数')),
            ],
            options={
                'db_table': 'duanzi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('bid', models.AutoField(primary_key=True, serialize=False, verbose_name='文章id')),
                ('btitle', models.CharField(max_length=254, verbose_name='标题')),
                ('btext', mdeditor.fields.MDTextField(verbose_name='正文')),
                ('btime', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('bfavour', models.IntegerField(blank=True, default=0, null=True, verbose_name='获赞数')),
                ('bbrowse', models.IntegerField(blank=True, default=0, null=True, verbose_name='浏览数')),
                ('bcomment', models.IntegerField(blank=True, default=0, null=True, verbose_name='评论数')),
            ],
            options={
                'db_table': 'blog',
            },
        ),
    ]
