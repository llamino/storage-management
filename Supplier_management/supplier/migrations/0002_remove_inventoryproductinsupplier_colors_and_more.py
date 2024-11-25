# Generated by Django 5.1.3 on 2024-11-21 13:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventoryproductinsupplier',
            name='colors',
        ),
        migrations.RemoveField(
            model_name='inventoryproductinsupplier',
            name='sizes',
        ),
        migrations.AddField(
            model_name='inventoryproductinsupplier',
            name='colors',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='supplier.colorsupplier'),
        ),
        migrations.AddField(
            model_name='inventoryproductinsupplier',
            name='sizes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='supplier.sizesuppler'),
        ),
    ]