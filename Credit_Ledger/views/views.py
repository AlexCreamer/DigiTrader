from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the credits index in the views directory")

def person_detail(request, person_id, person_name, account_id):
    return HttpResponse(
        "You are looking at the persons id %s, person name %s,and persons account number %s" %
        person_id, person_name, account_id)

def account_detail(request, account_id, balance, account_type):
    return HttpResponse(
        "You are looking at the account id %s, balance %s,and account type %s" %
        account_id, balance, account_type)
