from django.db import models
from rest_framework.authtoken.admin import User


class DiscountPerProduct(models.Model):  #this class is discount per product that define in the product service
    product_id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=50)
    discount_percent = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    stock = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)

class DiscountPerCategroyAndUser(models.Model):
    category_id = models.CharField(max_length=50)
    users = models.ManyToManyField(User, through='DiscountCodeUser', related_name='discounts')
    code = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    discount_percent = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)

class DiscountCodeUser(models.Model):  # this class is link class between User and DiscountPerCategoryAndUser
    discount = models.ForeignKey(DiscountPerCategroyAndUser, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)

# Create your models here.
