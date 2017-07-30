from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views import generic
from .forms import UserForm

from .models import Account

class IndexView(generic.ListView):
    template_name = "Credit_Ledger/index.html"
    context_object_name = "object_list"

    def get_queryset(self):
        return Account.objects.all()

#ex: /account_id/2
class DetailView(generic.DetailView):
    template_name = "Credit_Ledger/account_id.html"
    model = Account

    def get_queryset(self):
        return Account.objects.

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['account_id'] = self.kwargs['pk']
        return context

def person_detail(request, person_id):
    return HttpResponse(
        "You are looking at the persons id %s" % person_id)

def account_detail(request, account_id):
    template = loader.get_template("Credit_Ledger/account_id.html")
    context = {
        "account_id" : account_id,
    }
    return HttpResponse(template.render(context, request))

#ex /create_account/10
def CreateAccountView(request):
    new_account = Account(balance = 0, account_type = "regular")
    new_account.save()

    template = loader.get_template("Credit_Ledger/create_user.html")
    context = {
        "account_id" : new_account.id,
        "balance": 0,
        "type": "regular",
    }
    return HttpResponse(template.render(context, request))

class UserFormView(View):
    form_class = UserForm
    template_name = "Credit_Ledger/registration_form.html"

    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return rener(request, self.template_name)

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # normalized (clean) data
            username = form.cleaned_data["username"]
            passsword = form.cleaned_data["username"]


def auth_login(request):
    template = loader.get_template("registration/login.html")
    context = {}
    return HttpResponse(template.render(context, request))

def auth_password_reset(request):
    template = loader.get_template("registration/password_reset_form.html")
    context = {}
    return HttpResponse(template.render(context, request))

def auth_logout(request):
    template = loader.get_template("registration/logout.html")
    context = {}
    return HttpResponse(template.render(context, request))
