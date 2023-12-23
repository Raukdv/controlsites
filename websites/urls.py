#django modules
from django.urls import include, path

#project modules
from websites import views

urlpatterns = [
#Home Patterns
    path(
        '',
        views.ListWebsiteView.as_view(),
        name='websites_list'
    ),
    #Detail Pattern
    path(
        'control/detail/<int:pk>',
        views.WebsiteDetailView.as_view(),
        name='website_control_detail'
    ),
    path(
        'control/dns/<int:pk>',
        views.WebsiteDNSView.as_view(),
        name='website_dns_information'
    ),
    #Get Form website for custom HTML
    path(
        'control/getting-form-website',
        views.WebsiteCustomFormView.as_view(),
        name='website_control_custom_form'
    ),
]