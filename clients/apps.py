from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class ClientsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clients'



# apps.py
from django.apps import AppConfig

class ClientsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clients'

    def ready(self):
        import clients.signals  # ربط الإشارات عند بدء تشغيل التطبيق


class SuitConfig(DjangoSuitConfig):
    layout = 'vertical'