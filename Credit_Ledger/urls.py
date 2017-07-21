from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /credits/
    url(r'^$', views.index, name='index'),
    # ex: /credits/5/
    url(r'^(account_id/[0-9]+)/$', views.account_detail, name='detail'),

]
