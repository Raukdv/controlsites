from django.db import models

# Create your models here.
from django.utils import timezone
from django.urls import reverse_lazy
#For admin propuse
# Status and Action

class Server(models.Model):

    websties_inside = models.ManyToManyField(
        'websites.Website',
        verbose_name="Websites",
        blank=True,
    )
    
    sip = models.CharField(
        blank=True, null=True, max_length=50, verbose_name="server ip"
    )

    sname = models.CharField(
        blank=True, null=True, max_length=50, verbose_name="server name"
    )

    create_date = models.DateTimeField(
        auto_now_add = True, 
        verbose_name="create date"
    )

    user_ssh = models.CharField(
        blank=True, null=True, max_length=50, verbose_name="user ssh"
    )

    password_ssh = models.CharField(
        blank=True, null=True, max_length=100, verbose_name="password ssh"
    )

    description = models.TextField(
        max_length=700, 
        verbose_name="Description", 
        blank=False, 
        null=False
    )

    def __str__(self) -> str:
        return self.sname

    class Meta:
        ordering = ['create_date']
        verbose_name = "server"
        verbose_name_plural = "servers"