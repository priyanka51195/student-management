# Generated by Django 4.0 on 2021-12-29 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='number',
            field=models.IntegerField(max_length=10),
        ),
    ]
