from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register([user,client,suplier])
admin.site.register([approved_invoice,request_invioce])
