from django import forms
from django.contrib.auth.models import User
from employees.models import Employee


class RegistrationForm(forms.Form):

    username = forms.CharField(max_length=150,help_text="Enter a unique username")
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    department = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)

    def clean_username(self):
        username= self.cleaned_data["username"]

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("username already exits")
        return username

class LoginForm(forms.Form):

    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)