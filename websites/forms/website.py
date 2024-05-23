from django import forms

from websites.models.website import Website
from websites.tools.checking import is_valid_hostname
from django.core.exceptions import ValidationError

class WebsitesForm(forms.ModelForm):

    domain = forms.CharField(required=True, label='domain', 
            widget = forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'domain',
            }
        )
    )

    user = forms.CharField(required=False, label='user', 
            widget = forms.TextInput(attrs={
                'class':'form-control', 
                'placeholder':'user',
            }
        )
    )

    password = forms.CharField(required=False, label='password',
            widget = forms.TextInput(attrs={
                'class':'form-control', 
                'placeholder':'password',
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data:
            raise ValidationError("The Content is empty!")
        
        #validate if domain/hostname is not full/canonical url
        domain = cleaned_data.get('domain')
        
        if not is_valid_hostname(domain):
            self.add_error('domain', 'The domain is not valid.')
        
        return cleaned_data

    class Meta:
        model = Website
        fields  = [
            'domain', 
            'user', 
            'password'
        ]