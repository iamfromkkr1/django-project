# Generated by Django 4.0.5 on 2022-06-25 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='date_jioned',
            new_name='date_joined',
        ),
    ]
