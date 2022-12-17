from django.contrib import admin

# Register your models here.
from .models import House


class HouseAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "address", "price", "rooms", "created_by"]


admin.site.register(House, HouseAdmin)
