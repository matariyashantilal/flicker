from django import forms
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm

from .models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class UserCreationForm(BaseUserCreationForm):
    error_messages = {
        'password_mismatch': "Your passwords must match",
    }
    password1 = forms.CharField(error_messages={
                                'required': 'A password is required.'}, widget=forms.PasswordInput)
    password2 = forms.CharField(error_messages={
        'required': 'Confirm password is required.'}, widget=forms.PasswordInput)
  

    class Meta:
        model = User
        fields = ('email', 'password1')
        error_messages = {
            'email': {
                'required': _("Your email address is required."),
                'unique': _("This email is already registered"),
            },
        }

    