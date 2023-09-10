from django import forms

from websites.models.website import Website


class WebsitesForm(forms.ModelForm):

    domain = forms.CharField(required=True, label='domain', 
            widget = forms.TextInput(attrs={
                'class':'form-control',
                'placeholder': 'domain',
            }
        )
    )

    user = forms.CharField(required=False, label='user', 
            widget = forms.TextInput(attrs={
                'class':'form-control', 
                'placeholder': 'user',
            }
        )
    )

    password = forms.CharField(required=False, label='password',
            widget = forms.TextInput(attrs={
                'class':'form-control', 
                'placeholder': 'password',
            }
        )
    )

    class Meta:
        model = Website
        fields  = [
            'domain', 
            'user', 
            'password'
        ]
        