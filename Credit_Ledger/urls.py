from django.conf.urls import include, url
from registration.backends.simple.views import RegistrationView

from . import views


# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/'

urlpatterns = [
    # ex: /credits/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /credits/5/
    url(r'^account_id/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='account_detail'),
    url(r'^create_account/$', views.UserFormView, name='account_detail'),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/login/$', views.auth_login , name='auth_login'),
    url(r'^accounts/password_reset/$', views.auth_password_reset , name='auth_password_reset'),

]
