from django.contrib import admin
from .models import Client
from django.utils.html import format_html

class ClientAdmin(admin.ModelAdmin):
    list_display = ('الاسم', 'الموعد', 'الهاتف', 'الاقامة', 'القسم', 'نشط')
    list_display_links = ('الاسم',)
    search_fields = ('الاسم', 'الهاتف', 'الاقامة')

class CustomAdminSite(admin.AdminSite):
    def each_context(self, request):
        context = super().each_context(request)
        context['custom_css'] = 'css/custom_grappelli.css'
        return context

admin_site = CustomAdminSite(name='custom_admin')

admin.site.register(Client, ClientAdmin)
admin.site.site_header = 'Nouvil'
admin.site.site_title = 'Nouvil'