# Generated by Django 4.1 on 2022-09-04 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_helpdeskcontact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'permissions': (('add_product_to_cart', 'Add product to cart'),)},
        ),
    ]