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
            passsword = form.cleaned_data["password"]


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

# Create a new class that redirects the user to the index page, if successful at registering
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request):
        return '/'

    #This function was taken from Llennox at https://github.com/llennox/users/blob/master/views.py
    def register(self, request):
        print (request)
        email_taken = False
        username_taken = False
        if request.user.is_authenticated():
            return render(request, "index.html")
        registration_form = RegistrationForm()
        if request.method == 'POST':
            if form.is_valid():
                datas = {}
                if User.objects.filter(username=form.cleaned_data['username']).exists():
                   username_taken = True
                   return render (request, 'registration/registration_form', {'form':registration_form,'username_taken': username_taken})
                elif User.objects.filter(email=form.cleaned_data['email']).exists():
                    email_taken = True
                    return render(request, 'registration/registration_form', {'form':registration_form,'email_taken': email_taken})
                datas['username']=form.cleaned_data['username']
                datas['email']=form.cleaned_data['email']
                datas['password1']=form.cleaned_data['password1']
                salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
                usernamesalt = datas['email']
                if isinstance(usernamesalt, str):
                     usernamesalt=str.encode(usernamesalt)
                if isinstance(salt, str):
                     salt=str.encode(salt)
                
                datas['activation_key']=hashlib.sha1(salt+usernamesalt).hexdigest()
                datas['email_path']="/home/anox/sites/mc/static/ActivationEmail.txt"
                datas['email_subject']="activate your account"
                form.sendEmail(datas) #Send validation email
                form.save(datas) #Save the user and his profile
                request.session['registered']=True #For display purposes
                return render(request, 'registration/registration_form.html', {'email_sent':True})
        else:
            registration_form = form #Display form with error messages (incorrect fields, etc
            return render(request, 'registration/registration_form.html', {'form':registration_form})
                  
        if form.is_valid():
            username = (form.cleaned_data['username'])
        print ("Hello world")


