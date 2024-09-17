from django.db import models

class Client(models.Model):
    الاسم = models.CharField(max_length=100)
    
    # تحديد max_digits و decimal_places
    الموعد = models.CharField(max_length=100)
    
    الهاتف = models.CharField(max_length=12)
    الاقامة = models.CharField(max_length=12)
    الايصال = models.ImageField(upload_to='photos/Xy/Xm/%d')

    # زر منسدل
    CATEGORY_CHOICES = [
        ('option1', 'المالية'),
        ('option2', 'المشتريات'),
        ('option3', 'HR'),
    ]
    
    القسم = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='option1')

    نشط = models.BooleanField(default=True)

    def __str__(self):
        return self.الاسم
    
