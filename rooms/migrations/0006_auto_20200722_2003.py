# Generated by Django 2.2.5 on 2020-07-22 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20200722_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='romm_type',
            new_name='room_type',
        ),
    ]
