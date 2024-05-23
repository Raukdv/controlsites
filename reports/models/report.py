from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy

import uuid
from reports import constants

#For admin propuse
# Status and Action

class Report(models.Model):

    uuid = models.UUIDField(
        editable=False, 
        default=uuid.uuid4, 
        unique=True
    )

    from_website = models.ForeignKey(
        'websites.Website',
        on_delete=models.CASCADE,
        verbose_name="Website"
    )

    http_status = models.CharField(
        choices=constants.HTTPS_STATUS,
        default=constants.HTTPS_STATUS_DEFAULT,
        verbose_name="Http Status Code"
    )
    
    status = models.CharField(
        choices=constants.STATUS,
        default=constants.STATUS_DEFAULT,
        verbose_name="Status"
    )

    request_of = models.CharField(
        choices=constants.REQUEST_OF,
        default=constants.REQUEST_OF_DEFAULT,
        verbose_name="Request of"
    )

    incident_date = models.DateTimeField(
        auto_now_add = True, 
        verbose_name="incident date"
    )

    description = models.TextField(
        max_length=700, 
        verbose_name="Description", 
        blank=False, 
        null=False
    )

    action = models.TextField(
        blank=True, 
        null=True
    )

    image = models.ImageField(
        upload_to='media/incidents', 
        blank=True, 
        null=True
    )

    @property
    def img_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def __str__(self) -> str:
        return self.from_website.domain
    
    def get_absolute_report_detail_url(self):
        return reverse_lazy('reports:report_detail', args=[self.pk])

    class Meta:
        ordering = ['incident_date']
        verbose_name = "report"
        verbose_name_plural = "reports"