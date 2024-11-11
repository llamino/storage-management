from django.db import models
from setuptools._distutils._collections.RangeMap import Item



class Order(models.Model):
    user_id = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    pub_at = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user_id


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.IntegerField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product.name


# Create your models here.
