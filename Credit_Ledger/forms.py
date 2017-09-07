from django.contrib.auth.models import User
from django import forms

class UserForm(forms.Form):
    user = forms.CharField(label='User to trade with', max_length=100)
    amount = forms.IntegerField(label='Amount to trade')