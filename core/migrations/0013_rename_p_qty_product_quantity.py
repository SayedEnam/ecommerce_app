# Generated by Django 5.0.6 on 2024-12-23 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_product_p_qty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='p_qty',
            new_name='quantity',
        ),
    ]