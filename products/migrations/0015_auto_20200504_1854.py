# Generated by Django 2.2.4 on 2020-05-04 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_profile_wishlist_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='products',
            new_name='cart_products',
        ),
    ]