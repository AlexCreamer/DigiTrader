from django.contrib.auth.models import User
from django import forms

class UserForm(forms.Form):
    pk = forms.IntegerField(label='User to trade with', widget=forms.Textarea)
    amount = forms.IntegerField(label='Amount to trade', widget=forms.Textarea)
    
class GrantForm(forms.Form):
    pk = forms.IntegerField(label='User to grants credits to', widget=forms.Textarea)
    amount = forms.IntegerField(label='Amount to grant', widget=forms.Textarea)