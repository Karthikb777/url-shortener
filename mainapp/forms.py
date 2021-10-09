from django import forms
from .models import url
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class newUrlForm(forms.ModelForm):
    class Meta:
        model = url
        fields = ['full_url', 'ext']
        widgets = {
            'full_url': forms.TextInput(attrs={'class': 'uk-input uk-form-width-large', 'placeholder': 'Enter full URL'}),
            'ext': forms.TextInput(attrs={'class': 'uk-input uk-form-width-large', 'placeholder': 'Enter short UID'}),
        }


# user authentication forms

# form to log a user in
class LoginForm(forms.Form):
    username = forms.CharField(max_length=200, required=True)
    password = forms.CharField(max_length=200, required=True, widget=forms.PasswordInput())


# form to create a new user i.e registering a new user
class CreateUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")



