from django.db import models

# Create your models here.
class Account(models.Model):
    balance = models.DecimalField(max_digits=30, decimal_places=6)
    account_type = models.CharField(max_length=100)


class Person(models.Model):
    name = models.CharField(max_length=200)
    account_id = models.ForeignKey(Account)
