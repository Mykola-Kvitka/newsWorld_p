# Generated by Django 3.1.7 on 2021-04-29 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_auto_20210429_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(),
        ),
    ]
