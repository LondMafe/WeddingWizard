# Generated by Django 5.0.4 on 2024-05-31 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='expirationDate',
            field=models.DateField(),
        ),
    ]
