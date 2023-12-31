from django import forms
from reports.models import Report

class ReportFormModel(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Report
        