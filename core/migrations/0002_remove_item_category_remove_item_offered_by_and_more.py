# Generated by Django 5.0.4 on 2024-05-26 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='category',
        ),
        migrations.RemoveField(
            model_name='item',
            name='offered_by',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='vendor_id',
            new_name='vendor_identifier',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
