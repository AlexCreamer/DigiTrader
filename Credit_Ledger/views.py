from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views import generic
from .forms import UserForm
from registration.backends.simple.views import RegistrationView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Account

from .models import Account

#ex: /account_id/2
class AccountDetail(generic.DetailView):
    template_name = "Credit_Ledger/account_details.html"
    model = Account
    
    def get_queryset(self):
         account_objects = Account.objects.all()
         pk = int(self.kwargs['pk'])   
    
         my_object = get_object_or_404(User, pk=pk)
        
         queryset = account_objects.filter(pk=my_object.account.id)
         return queryset

    def get_context_data(self, **kwargs):
        print ("testing")
        context = super(AccountDetail, self).get_context_data(**kwargs)
        queryset = self.get_queryset()
        context['account_id'] = queryset[0].id
        context['balance'] = queryset[0].balance
        context['account_type'] = queryset[0].account_type
        return context


class IndexView(generic.ListView):
    template_name = "Credit_Ledger/index.html"
    context_object_name = "object_list"

    def get_queryset(self):
        account_objects = Account.objects.all()
        user = self.request.user
        account_pk = user.account.id
            
        return account_objects.filter(pk=account_pk)
        
    def get_context_data(self, **kwargs):
        user = self.request.user
        pk = user.id
        
        if pk == None:
            return None
        elif pk > 0:
            context = super(IndexView, self).get_context_data(**kwargs)
            queryset = self.get_queryset()
            if queryset == None:
                return context
            else:
                context['account_id'] = queryset[0].id
                context['balance'] = queryset[0].balance
                context['account_type'] = queryset[0].account_type
            return context
        else:
            raise Exception("User id is not None and is not greater than 0")

def account_detail(request, account_id):
    template = loader.get_template("Credit_Ledger/account_id.html")
    context = {
        "account_id" : account_id,
    }
    return HttpResponse(template.render(context, request))