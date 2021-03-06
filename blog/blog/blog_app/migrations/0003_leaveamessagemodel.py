# Generated by Django 2.2 on 2020-08-12 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_auto_20200804_0936'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaveAMessageModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(verbose_name='内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='时间')),
                ('username', models.CharField(max_length=30, verbose_name='用户')),
            ],
            options={
                'db_table': 'leave_a_message',
            },
        ),
    ]
