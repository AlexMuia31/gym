# Generated by Django 3.0.6 on 2020-05-19 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200519_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='category',
        ),
        migrations.AddField(
            model_name='user',
            name='category',
            field=models.CharField(choices=[('BodyBuilding', 'BodyBuilding'), ('Fitness', 'Fitness'), ('Weight Lifting', 'Weight Lifting'), ('Boxing', 'Boxing')], default='', max_length=20),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='categorie',
        ),
    ]
