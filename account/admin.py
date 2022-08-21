from django.contrib import admin
from .models import Account
# from django.contrib.auth.admin import UserAdmin
# # Register your models here.

class AccountAdmin( admin.ModelAdmin ):
    list_display = [field.name for field in Account._meta.fields]

admin.site.register( Account, AccountAdmin )