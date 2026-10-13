from django import forms
from .models import Employee

class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=["department","phone","profile_photo"]