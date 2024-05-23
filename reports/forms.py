from django import forms
from reports.models import Report

from reports import constants

class ReportFormModel(forms.ModelForm):

    #def __init__(self, *args, **kwargs):
        #super(ReportFormModel, self).__init__(*args, **kwargs)
        # assign a (computed, I assume) default value to the choice field
        #self.initial['http_status'] = '200'
        # you should NOT do this:
        #self.fields['choices_field_name'].initial = 'default value'

    from_website = forms.ModelChoiceField(
            queryset=Report.objects.all(), 
            required=False, 
            label='Websites',
            help_text='Choose a website to request',
            widget = forms.Select(attrs={
                'class':'form-select mt-2',
                }
            )
        )
    
    http_status = forms.ChoiceField(
            label='HTTP Status',
            choices=constants.HTTPS_STATUS,
            required=False,
            initial='200',
            help_text='Select one if you know it, if not check this Reference List: <a href="/reports/http-ref">HTTPS</a>',
            widget= forms.Select(
                attrs= {
                'class':'form-select mt-2'
            }
        )
    )

    request_of = forms.ChoiceField(
            label='Request Type',
            choices=constants.REQUEST_OF,
            required=False,
            initial='REQUEST_CHECK',
            help_text='Which request do you want to do?',
            widget= forms.Select(attrs= {
                'class':'form-select mt-2'
            }
        )
    )

    description = forms.CharField(
        label='Description',
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control mt-2',
            'type':'text',
            'placeholder':'Description',
            'cols':'55',
            'rows':'5'
            }
        )
    )

    image = forms.ImageField(
        label='Image', 
        help_text="Just JPEG/JPG or PNG will be saved", 
        widget=forms.ClearableFileInput(attrs={
            'multiple': False
            }
        )
    )
    
    class Meta:
        model=Report
        fields=(
            'from_website',
            'request_of',
            'http_status',
            'description',
            'image'
        )
        