# Generated by Django 4.0.5 on 2022-07-08 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='userprofile'),
        ),
    ]