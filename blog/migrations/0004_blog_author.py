# Generated by Django 3.0.6 on 2020-05-22 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200517_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
