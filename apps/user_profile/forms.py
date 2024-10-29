from typing import Any
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, update_session_auth_hash
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


class AuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """

    username = forms.CharField(
        label="Логин",
        widget=forms.TextInput(attrs={"autofocus": True, "class": "form-control"}))
    password = forms.CharField(
        label="Пароль",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class": "form-control"}),
    )


    def __init__(self, request=None, *args, **kwargs):
        """
        The 'request' parameter is set for custom auth use by subclasses.
        The form data comes in via the standard 'data' kwarg.
        """
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username is not None and password:
            self.user_cache = authenticate(
                self.request, username=username, password=password
            )
            if self.user_cache is None:
                raise ValidationError('Неправильный логин или пароль')

        return self.cleaned_data


class RegisterForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password_one = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password_two = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))


    def clean(self) -> dict[str, Any]:
        password_one = self.cleaned_data.get('password_one')
        password_two = self.cleaned_data.get('password_two')
        if password_one != password_two:
            raise ValidationError('Пароли не совпадают!')

    def clean_username(self):
        User = get_user_model()
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise ValidationError('такой пользователь уже есть')
        return username
    

class ChangePssword(forms.Form):

    old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password_one = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password_two = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))


    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
    
    def clean(self) -> dict[str, Any]:
        password_one = self.cleaned_data.get('password_one')
        password_two = self.cleaned_data.get('password_two')
        if password_one != password_two:
            raise ValidationError('Пароли не совпадают!')

    def clean_old_password(self):
        password = self.cleaned_data.get('old_password')
        if not self.user.check_password(password):
            raise ValidationError('Неверный пароль')