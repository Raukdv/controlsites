from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy

import uuid
import constants

class Report(models.Model):
    uuid = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)

    from_website = models.ForeignKey(
        'websites.Website',
        on_delete=models.CASCADE,
        verbose_name="Website"
    )

    incident_date = models.DateTimeField(
        auto_now_add = True, 
        verbose_name="incident date"
    )

    description = models.TextField(max_length=700, verbose_name="Content", blank=False, null=False)

    http_status = models.CharField(
        choices=constants.HTTPS_STATUS,
        default=constants.HTTPS_STATUS_DEFAULT,
        verbose_name="Http Status Code"
    )

    action = models.TextField(
        blank=True, 
        null=True
    )

    status = models.CharField(
        choices=constants.HTTPS_STATUS,
        default=constants.HTTPS_STATUS_DEFAULT,
        verbose_name="Http Status Code"
    )

    image = models.ImageField(
        upload_to='images/incidents', 
        blank=True, 
        null=True
    )