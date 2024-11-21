from django.utils.text import slugify
from django.utils.timezone import now

from django.db import models

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    date_of_establishment = models.DateField(auto_now_add=True)
    is_full = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.name)
            self.slug = slug
        super(Warehouse, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title

class Employee(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='employees')
    tasks = models.ManyToManyField(Task, through='TaskForEmployee', related_name='employees')
    manager = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='employees')
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    national_code = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name

# Create your models here.
class TaskForEmployee(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    was_delivered_at = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.employee} {self.task} {self.was_delivered_at}'



class Inventory(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='inventories')
    product_id = models.IntegerField() # foreign key from ProductProperty table in the Product service
    stock = models.IntegerField()
class PurchaseOrderFromSupplier(models.Model):
    supplier_id = models.IntegerField() # foreign key from Supplier table in the supplier service
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='suppliers')
    order_date = models.DateField(auto_now_add=True)
    expected_delivery_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.supplier_id} - {self.warehouse} '

class PurchaseOrderDetails(models.Model):
    purchase_order_from_supplier = models.ForeignKey(PurchaseOrderFromSupplier, on_delete=models.CASCADE, related_name='order_details')
    product_In_Supplier = models.IntegerField() # foreign key from InventoryProductInSupplier table in the Supplier service
    quantity_ordered = models.IntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f'{PurchaseOrderFromSupplier} - {self.product_In_Supplier} - {self.quantity_ordered} '



