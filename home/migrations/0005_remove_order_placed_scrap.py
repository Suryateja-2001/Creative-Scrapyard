# Generated by Django 4.1 on 2023-02-10 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_cart_scrap'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_placed',
            name='scrap',
        ),
    ]
