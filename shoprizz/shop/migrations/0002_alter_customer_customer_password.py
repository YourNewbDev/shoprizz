# Generated by Django 4.2.4 on 2023-10-16 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_password',
            field=models.CharField(max_length=12),
        ),
    ]
