# Generated by Django 4.2.16 on 2024-11-18 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='tax',
            field=models.FloatField(null=True),
        ),
    ]
