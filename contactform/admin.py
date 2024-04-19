from django.contrib import admin
from .models import ContactMessage

class ConatctFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'subject', 'message')
    search_fields = ('name', 'email', 'phone', 'subject', 'message')
    list_filter = ('subject',)

admin.site.register(ContactMessage, ConatctFormAdmin)