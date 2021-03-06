# Generated by Django 3.0.6 on 2020-05-17 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Body', models.TextField(max_length=10000)),
                ('Picture', models.ImageField(upload_to='images/')),
                ('pub_date', models.DateTimeField()),
            ],
        ),
    ]
