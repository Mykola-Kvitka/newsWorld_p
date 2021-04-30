# Generated by Django 3.2 on 2021-04-27 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorName', models.TextField()),
                ('commentBody', models.CharField(max_length=200)),
                ('dateTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('username', models.TextField()),
                ('email', models.TextField(default='')),
                ('ip', models.TextField(default='')),
                ('time', models.TimeField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('short_txt', models.TextField()),
                ('body_txt', models.TextField()),
                ('date', models.CharField(max_length=12)),
                ('writer', models.CharField(max_length=100)),
                ('show', models.IntegerField(default=0)),
                ('topicId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=50)),
                ('creationDate', models.DateField()),
            ],
        ),
    ]
