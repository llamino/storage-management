from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# تنظیم نام برنامه Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
app = Celery('myproject')

# خواندن تنظیمات از فایل تنظیمات Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# جستجوی خودکار وظایف در اپلیکیشن‌ها
app.autodiscover_tasks()
