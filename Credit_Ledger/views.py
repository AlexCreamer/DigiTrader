from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views import generic
from .forms import UserForm
from registration.backends.simple.views import RegistrationView


from .models import Account

class IndexView(generic.ListView):
    template_name = "Credit_Ledger/index.html"
    context_object_name = "object_list"

    def get_queryset(self):
        return Account.objects.all()

#ex: /account_id/2
class AccountDetail(generic.DetailView):
    template_name = "Credit_Ledger/account_id.html"
    model = Account

    def get_queryset(self):
        all_objects = Account.objects.all()
        pk = int(self.kwargs['pk'])
        if pk > 0:
            if pk < len(all_objects):
                return all_objects.filter(pk=pk)
            else:
                return None
        else:
            return None

        return queryset

    def get_context_data(self, **kwargs):
        context = super(AccountDetail, self).get_context_data(**kwargs)
        queryset = self.get_queryset()
        context['account_id'] = queryset[0].id
        context['balance'] = queryset[0].balance
        context['account_type'] = queryset[0].account_type
        return context

def account_detail(request, account_id):
    template = loader.get_template("Credit_Ledger/account_id.html")
    context = {
        "account_id" : account_id,
    }
    return HttpResponse(template.render(context, request))