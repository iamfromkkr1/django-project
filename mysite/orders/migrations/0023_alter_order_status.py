# Generated by Django 4.0.5 on 2022-06-25 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Accepted', 'Accepted'), ('Cancelled', 'Cancelled'), ('New', 'New')], default='New', max_length=15),
        ),
    ]
