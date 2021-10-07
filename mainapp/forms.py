from django import forms
from .models import url


class newUrlForm(forms.ModelForm):
    class Meta:
        model = url
        fields = '__all__'
        widgets = {
            'full_url': forms.TextInput(attrs={'class': 'uk-input uk-form-width-large', 'placeholder': 'Enter full URL'}),
            'ext': forms.TextInput(attrs={'class': 'uk-input uk-form-width-large', 'placeholder': 'Enter short UID'}),
        }


