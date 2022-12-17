from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Accounts


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
    email = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control"}))

    class Meta:
        model = Accounts
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "is_owner",
            "is_tenant",
        )
