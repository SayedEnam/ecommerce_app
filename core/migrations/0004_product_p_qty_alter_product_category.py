# Generated by Django 5.0.6 on 2024-12-10 08:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_product_old_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='p_qty',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='core.category'),
        ),
    ]
