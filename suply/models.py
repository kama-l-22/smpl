from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class user(AbstractUser):
    is_bank = models.BooleanField(default=False)
    is_supplier = models.BooleanField(default=False)
    is_client  = models.BooleanField(default=False)


class client(models.Model):
    if user.is_client:
        name = models.OneToOneField(user, on_delete=models.CASCADE)
        client_id = models.CharField(max_length=50,null = True, blank=True)
        loan_id = models.CharField(max_length=50,null = True, blank=True)


class suplier(models.Model):
    if user.is_supplier:
        name = models.OneToOneField(user, on_delete=models.CASCADE)
        sup_id = models.CharField(max_length=50,null = True, blank=True)
        
class request_invioce(models.Model):
    name = models.ForeignKey(user,on_delete=models.CASCADE)
    client_id = models.CharField(max_length=100)
    amount = models.IntegerField()
    cus_id = models.CharField(max_length=50)

class approved_invoice(models.Model):
   
    client_id = models.CharField(max_length=100)
    amount = models.IntegerField()
    cus_id = models.CharField(max_length=50)
    approved_by = models.CharField(max_length=100)
    sup_id = models.CharField(max_length=100)