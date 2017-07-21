from django.http import HttpResponse

from .models import Account

def index(request):
    return HttpResponse("Hello, world. You're at the credits index in the views directory")

def person_detail(request, person_id):
    return HttpResponse(
        "You are looking at the persons id %s" % person_id)

def account_detail(request, account_id):
    template = loader.get_template("Credit_Ledger/account_id.html")
    context = {
        "account_id" : account_id,
    }
    return HttpResponse(template.render(context, request))
