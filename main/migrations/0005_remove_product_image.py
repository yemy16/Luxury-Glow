# Generated by Django 5.1.1 on 2024-09-16 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]