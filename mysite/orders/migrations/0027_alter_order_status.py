# Generated by Django 4.0.5 on 2022-06-27 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0026_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled'), ('Completed', 'Completed'), ('Accepted', 'Accepted'), ('New', 'New')], default='New', max_length=15),
        ),
    ]
