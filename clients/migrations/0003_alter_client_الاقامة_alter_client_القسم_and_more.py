# Generated by Django 5.0.6 on 2024-09-10 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_alter_client_الموعد'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='الاقامة',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='client',
            name='القسم',
            field=models.CharField(choices=[('option1', 'المالية'), ('option2', 'المشتريات'), ('option3', 'HR')], default='option1', max_length=20),
        ),
        migrations.AlterField(
            model_name='client',
            name='الموعد',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='client',
            name='الهاتف',
            field=models.IntegerField(),
        ),
    ]
