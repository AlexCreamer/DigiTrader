from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /credits/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /credits/5/
    url(r'^account_id/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='account_detail'),
    url(r'^create_account/$', views.UserFormView, name='account_detail'),
]
