from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True, default="000000000")
    national_code = models.CharField(max_length=10, unique=True, blank=True, null=True, verbose_name="کد ملی")
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True, verbose_name="تصویر پروفایل")

    def __str__(self):
        return self.username

class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    province = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    street = models.CharField(max_length=50, blank=True, null=True)
    alley = models.CharField(max_length=50, blank=True, null=True)
    house_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} {self.id}'