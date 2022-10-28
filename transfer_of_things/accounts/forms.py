from django.contrib.auth import get_user_model, authenticate
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import AbstractUser
from django.forms import ModelForm

from .models import CustomUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class UserAdminCreationForm(UserCreationForm):
    """A custom form for creating new users."""

    required_css_class = "form-group"
    first_name = forms.CharField(widget=forms.TextInput)
    last_name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-group'}),
        }

    def __init__(self, *args, **kwargs):
        """
        Change/mark user fields tags and widgets.
        """
        super().__init__(*args, **kwargs)
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Nazwisko'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Imię'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Hasło'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Powtórz hasło'})
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        for field in self.fields:
            print(field)
            self.fields[str(field)].label = ''


# class UserAuthenticationForm(ModelForm):
#     required_css_class = "form-group"
#
#     class Meta:
#         model = CustomUser
#         fields = ['email', 'password']
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.user = None
#         self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
#         self.fields['password'].widget.attrs.update({'placeholder': 'Hasło'})
#         for field in self.fields:
#             print(field)
#             self.fields[str(field)].label = ''
#
#     def clean(self):
#         cd = super().clean()
#         email = cd.get('email')
#         password = cd.get('password')
#         self.user = authenticate(email=email, password=password)
#         if self.user is None:
#             raise ValidationError('Podaj poprawne dane')


class LoginForm(forms.Form):
    """
    Create and change/mark a login form fields.
    """
    required_css_class = "form-group"
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    email.widget.attrs.update({'placeholder': 'Email'})
    email.label = ''
    password.widget.attrs.update({'placeholder': 'Hasło'})
    password.label = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    def clean(self):
        """
        Cleaned POST method data and authenticate user.
        Raise error if user data invalid .
        """
        cd = super().clean()
        email = cd.get('email')
        password = cd.get('password')
        self.user = authenticate(email=email, password=password)
        if self.user is None:
            raise ValidationError('Podaj poprawne dane')
