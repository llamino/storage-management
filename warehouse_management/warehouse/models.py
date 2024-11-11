from django.db import models

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    is_full = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.title

class Employee(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='employees')
    tasks = models.ManyToManyField(Task, through='TaskForEmployee')
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
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='tasks')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='tasks')
    was_delivered_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.employee} {self.task} {self.was_delivered_at}'



class Inventory(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='inventories')
    product_id = models.IntegerField() # کلید خارجی از جدول محصول در سرویس محصول
    stock = models.IntegerField()
class PurchaseOrderFromSuppplier(models.Model):
    supplier_id = models.IntegerField() # کلید خارجی از جدول تامین کننده در سرویس تامین کننده
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='suppliers')
    order_date = models.DateField(auto_now_add=True)
    expected_delivery_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.supplier_id} - {self.warehouse} '

class PurchaseOrderDetails(models.Model):
    purchase_order_from_supplier = models.ForeignKey(PurchaseOrderFromSuppplier, on_delete=models.CASCADE, related_name='order_details')
    product_In_Supplier = models.IntegerField() # کلید خارجی از جدول محصولات تامین کننده، در سرویس تامین کننده
    quantity = models.IntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f'{PurchaseOrderFromSuppplier} - {self.ProductInSupplier} - {self.quantity} '



class SupplierAndWarehouseTransactions(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='supplier_and_warehouse')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supplier_and_warehouse') # کلید خارجی جدول تامین کننده در سرویس تامین کننده
    product = models.ForeignKey(Inventory.product_id, on_delete=models.CASCADE, related_name='supplier_and_warehouse')

