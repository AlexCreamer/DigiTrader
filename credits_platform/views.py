from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic import View
from django.views import generic
from .forms import UserForm, GrantForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Account
from django.http import HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required

#ex: /account_id/2
class AccountDetail(generic.DetailView):
    template_name = "credits_platform/account_details.html"

    def get_queryset(self):
         account_objects = Account.objects.all()
         pk = int(self.kwargs['pk'])

         my_object = get_object_or_404(User, pk=pk)

         queryset = account_objects.filter(pk=my_object.account.id)
         return queryset

    def get_context_data(self, **kwargs):
        context = super(AccountDetail, self).get_context_data(**kwargs)
        queryset = self.get_queryset()
        context['account_id'] = queryset[0].id
        context['balance'] = queryset[0].balance
        context['account_type'] = queryset[0].account_type
        return context


class IndexView(generic.ListView):
    template_name = "credits_platform/index.html"
    context_object_name = "object_list"
    form_class = UserForm
    

    def get_queryset(self):
        account_objects = Account.objects.all()
        user = self.request.user
        if user.is_anonymous:
            return None
        else:
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
        
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})



def account_detail(request, account_id):
    template = loader.get_template("credits_platform/account_id.html")
    context = {
        "account_id" : account_id,
    }
    return HttpResponse(template.render(context, request))
    
def user_trade(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)

        # check whether it's valid:
        if form.is_valid():
            # redirect to a new URL:
            pk = form.cleaned_data["pk"]
            amount = form.cleaned_data["amount"]

            a = Account.objects.get(pk=request.user.id)
            if a.balance >= amount:
                a.balance = a.balance - amount
                a.save()

                b = Account.objects.get(pk=pk)
                b.balance = b.balance + amount
                b.save()

            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'credits_platform/index.html')

@staff_member_required
def user_grant(request):
    if request.method == 'POST':
        form = GrantForm(request.POST)

        if form.is_valid():
            pk = form.cleaned_data["pk"]
            amount = form.cleaned_data["amount"]
            

