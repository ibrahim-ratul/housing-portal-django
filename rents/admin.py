from django.contrib import admin

from .models import Rents


class RentAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'tenant', 'owner']


admin.site.register(Rents)
