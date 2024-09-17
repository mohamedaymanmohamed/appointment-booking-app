# pages/models.py
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    residence_number = models.CharField(max_length=50, default='N/A')  # تعيين قيمة افتراضية
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.name
