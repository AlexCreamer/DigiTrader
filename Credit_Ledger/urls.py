from django.conf.urls import include, url
from registration.backends.simple.views import RegistrationView
from django.contrib.auth import views as auth_views

from . import views


# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request):
        return '/'

urlpatterns = [
    # ex: /credits/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /credits/5/
    url(r'^account_id/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='account_detail'),
    url(r'^create_account/$', views.UserFormView, name='account_detail'),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/password_reset/$', views.auth_password_reset , name='auth_password_reset'),
    url(r'^accounts/login/$', auth_views.LoginView.as_view(), name='auth_login'),
    url(r'^accounts/logout/$', auth_views.LogoutView.as_view(), name='auth_logout'),
    url(r'^accounts/auth_password_change/$', auth_views.PasswordChangeView.as_view(), name='auth_password_change'),
    url(r'^accounts/auth_password_change_done/$', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),




]
