# Generated by Django 4.0 on 2021-12-28 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('ID', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('password', models.CharField(max_length=15)),
            ],
        ),
    ]