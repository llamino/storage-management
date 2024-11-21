from django.test import TestCase
from celery import shared_task

@shared_task
def my_daily_task():
    # کدی که باید اجرا شود
    print("وظیفه روزانه اجرا شد")

# Create your tests here.
