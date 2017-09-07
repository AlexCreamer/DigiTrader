from django.contrib.auth.models import User
from django import forms

class UserForm(forms.Form):
    user = forms.CharField(label='User trade', max_length=100)