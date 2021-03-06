# Generated by Django 3.1.7 on 2021-04-29 20:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_auto_20210429_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 4, 29, 20, 40, 42, 901786, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='news',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.RemoveField(
            model_name='news',
            name='topicId',
        ),
        migrations.AddField(
            model_name='news',
            name='topicId',
            field=models.ManyToManyField(help_text='Select a topick for this news', to='firstapp.Topic'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
