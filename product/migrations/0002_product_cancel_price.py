# Generated by Django 4.2.16 on 2024-11-14 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cancel_price',
            field=models.FloatField(null=True),
        ),
    ]
