from django import forms
from .models import Usersdata

class UserForm(forms.ModelForm):
    class Meta:
        model = Usersdata
        fields = ['Username', 'Password']