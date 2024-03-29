from django.contrib import admin

# Register your models here.
from django.contrib import admin
from account.models import profile, Payment

admin.site.register(profile)
admin.site.register(Payment)