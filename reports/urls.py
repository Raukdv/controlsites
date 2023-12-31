#django modules
from django.urls import include, path

#project modules
from reports import views

urlpatterns = [
#List home pattern
    path(
        '',
        views.ReportListView.as_view(),
        name='report_listview'
    ),
#Report Patterns
    path(
        'request',
        views.ReportFormView.as_view(),
        name='report_formview'
    ),
    # #Detail Pattern
    # path(
    #     'report/detail/<int:pk>',
    #     views.WebsiteDetailView.as_view(),
    #     name='website_control_detail'
    # ),
    # path(
    #     'report/list/<int:pk>',
    #     views.WebsiteDNSView.as_view(),
    #     name='website_dns_information'
    # ),
]