from allauth.account.signals import user_signed_up
from ..models import Account
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

def add_account(request, user, **kwargs):
    Account.objects.create(balance=0.0, account_type="regular", user=user) 
user_signed_up.connect(add_account)

@receiver(post_save, sender=User)
def add_account_superuser(sender, instance, **kwargs):
    User = get_user_model()
    if isinstance(instance, User):
        if instance.is_superuser:
            Account.objects.create(balance=0.0, account_type="regular", user=instance) 


#post_save.connect(add_account_superuser, sender="User")