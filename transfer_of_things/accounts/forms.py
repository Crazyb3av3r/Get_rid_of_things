from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm


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
