# Generated by Django 2.2.5 on 2020-07-23 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0010_auto_20200723_0048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='house_rule',
            new_name='house_rules',
        ),
    ]