# pages/admin.py
from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'residence_number', 'date', 'time')  # تأكد من استخدام الحقول الصحيحة

admin.site.register(Client, ClientAdmin)
