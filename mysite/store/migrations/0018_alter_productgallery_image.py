# Generated by Django 4.0.5 on 2022-06-28 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_alter_productgallery_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productgallery',
            name='image',
            field=models.ImageField(max_length=255, upload_to='store/products'),
        ),
    ]
