#django modules
from django.urls import include, path

#project modules
from panel import views

urlpatterns = [
    #Home Patterns
    path(
        '',
        views.IndexListWebsiteView.as_view(),
        name='index'
    ),
    #Detail Pattern
    path(
        'status/<int:pk>/',
        views.IndexWebsiteDetailView.as_view(),
        name='website_index_detail'
    ),
    #Search Pattern
    path(
        'searching/',
        views.IndexSearchWebsites.as_view(),
        name='website_index_search'
    ),
]