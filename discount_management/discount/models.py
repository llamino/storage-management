from django.db import models

class Discount(models.Model):
    code = models.CharField(unique=True, max_length=50)
    discount_percent = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    class Meta:
        abstract= True
        ordering= ['-discount_percent']

class ProductDiscount(Discount):  #this class is discount per product that define in the product service
    product_id = models.CharField(unique=True) #this field represent product name.




class CategoryDiscount(Discount):
    category_id = models.CharField(max_length=50)




class UserDiscount(models.Model):
    discount_per_category = models.ForeignKey(CategoryDiscount, on_delete=models.CASCADE)
    user_id = models.CharField()
# Create your models here.
