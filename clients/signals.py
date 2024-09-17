# signals.py
from django.db.models.signals import post_delete
from django.contrib.admin.models import LogEntry
from django.dispatch import receiver
from .models import Client

@receiver(post_delete, sender=Client)
def delete_client_log(sender, instance, **kwargs):
    LogEntry.objects.filter(object_id=instance.id).delete()
