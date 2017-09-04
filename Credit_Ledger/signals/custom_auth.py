from allauth.account.signals import user_signed_up

def add_account(request, user):
    print("testing")
    print(user)
user_signed_up.connect(add_account)
