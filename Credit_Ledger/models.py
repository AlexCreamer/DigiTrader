from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    balance = models.DecimalField(max_digits=30, decimal_places=6, default=Decimal(0.000000))
    account_type = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
class Test:
    def save(self, commit=True):
        print('Saving within Test class')

class Permit(Test):
    
    def save(self, *args, **kwargs):
        print('Saving within Permit class')
        super(Permit, self).save(*args, **kwargs)

p = Permit()
p.save()