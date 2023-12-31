from django.contrib import admin
from reports import models
# Register your models here.
@admin.register(models.Report)
class ReportsAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'incident_date',
    )

    search_fields = (
        '__str__',
    )