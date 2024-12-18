# Generated by Django 5.1.3 on 2024-11-16 05:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrderFromSupplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier_id', models.IntegerField()),
                ('order_date', models.DateField(auto_now_add=True)),
                ('expected_delivery_date', models.DateField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('date_of_establishment', models.DateField(auto_now_add=True)),
                ('is_full', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100)),
                ('national_code', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='warehouse.employee')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_In_Supplier', models.IntegerField()),
                ('quantity_ordered', models.IntegerField()),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('purchase_order_from_supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='warehouse.purchaseorderfromsupplier')),
            ],
        ),
        migrations.CreateModel(
            name='TaskForEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('was_delivered_at', models.DateTimeField(auto_now_add=True)),
                ('is_done', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.employee')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='warehouse.task')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='tasks',
            field=models.ManyToManyField(related_name='employees', through='warehouse.TaskForEmployee', to='warehouse.task'),
        ),
        migrations.AddField(
            model_name='purchaseorderfromsupplier',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suppliers', to='warehouse.warehouse'),
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventories', to='warehouse.warehouse')),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='warehouse.warehouse'),
        ),
    ]
