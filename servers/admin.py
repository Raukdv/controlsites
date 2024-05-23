from django.contrib import admin
from servers import models
# Register your models here.

@admin.register(models.Server)
class ServersAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'sip',
        'create_date',
    )

    search_fields = (
        '__str__',
        'sip',
    )