from django.db import models
from pip._vendor.rich.color import Color



class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class SizeSuppler(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class ColorSupplier(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
# Create your models here.
class ProductInSupplier(models.Model):
    name = models.CharField(max_length=100)
    weight = models.IntegerField()
    content = models.TextField()
    price = models.IntegerField()
    categories = models.ManyToManyField(Category)
    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class InventoryProductInSupplier(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductInSupplier, on_delete=models.CASCADE)
    stock = models.IntegerField()
    colors = models.ManyToManyField(ColorSupplier)
    sizes = models.ManyToManyField(SizeSuppler)
    def __str__(self):
        return f'{self.supplier} - {self.product} - {self.stock}'