"""
URL configuration for controlsites project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

#global admin django
urlpatterns = [
    path('admin/', admin.site.urls),
]

#Modules Control Access Urls
urlpatterns += [
    path(
        '',
        include(('panel.urls', 'panel'), namespace='panel')
    ),
    path(
        'websites/',
        include(('websites.urls', 'websites'), namespace='websites')
    ),
    path(
        'reports/',
        include(('reports.urls', 'reports'), namespace='reports')
    ),
    path(
        'servers/',
        include(('servers.urls', 'servers'), namespace='servers')
    )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)