from django.contrib import admin
from websites import models
# Register your models here.

@admin.register(models.Website)
class WebsitesAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'pub_date',
    )

    search_fields = (
        '__str__',
    )