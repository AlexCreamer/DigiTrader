from django.contrib.auth.models import User
from django import forms

class UserForm(forms.Form):
    pk = forms.IntegerField(label='User to trade with')
    amount = forms.IntegerField(label='Amount to trade')
    
class GrantForm(forms.Form):
    pk = forms.IntegerField(label='User to grants credits to', widget="Textarea")
    amount = forms.IntegerField(label='Amount to grant', widget="Textarea")