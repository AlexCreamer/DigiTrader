from allauth.account.signals import user_signed_up
from ..models import Account


def add_account(request, user, **kwargs):
    Account.objects.create(balance=0.0, account_type="regular", user=user) 
    print(user)
user_signed_up.connect(add_account)
