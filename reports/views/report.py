from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone

#Mixin Auth system
from django.contrib.auth.mixins import LoginRequiredMixin

#Decorators
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

#CBV
from django.views.generic import (
    ListView,
    DetailView,
    FormView
)

from .. import forms
from ..models.report import Report

class ReportFormView(FormView):
    template_name = 'reports/report_formview.html'
    form_class = forms.ReportFormModel
    success_url = ''

class ReportListView(ListView):
    template_name = 'reports/reports_list.html'
    context_object_name = 'reports_list'

    def get_queryset(self):
        return Report.objects.all()

class ReportDetailView(DetailView):
    pass
