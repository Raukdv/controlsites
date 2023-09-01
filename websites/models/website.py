from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy


import datetime
from websites.tools.checking import(
    ssl_check,
    website_code_status
)

class Website(models.Model):

    domain = models.CharField(
        max_length = 200,
        blank=False, 
        null=True,
        verbose_name="domain"
    )

    pub_date = models.DateTimeField(
        auto_now_add = True, 
        verbose_name="date published"
    )

    user = models.CharField(
        blank=True, null=True, max_length=50, verbose_name="user"
    )

    password = models.CharField(
        blank=True, null=True, max_length=100, verbose_name="password"
    )

    @property
    def formated_domain(self):
        ssl_status = ssl_check(self.domain)
        domain = f'https://{self.domain}/' if ssl_status else f'http://{self.domain}/'
        return domain
        
    @property
    def ssl_enable(self):
        return ssl_check(self.domain)

    def __str__(self) -> str:
        return self.domain
    
    def was_published_recently(self) -> bool:
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def get_absolute_url(self):
        return reverse_lazy('panel:website_index_detail', args=[self.pk])
    
    class Meta:
        ordering = ['pub_date']
        verbose_name = "website"
        verbose_name_plural = "websites"