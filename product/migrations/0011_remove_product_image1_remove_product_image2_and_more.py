# Generated by Django 4.2.16 on 2024-12-10 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_product_image1_product_image2_product_image3_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image4',
        ),
    ]
