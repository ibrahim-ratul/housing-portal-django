from django.conf import settings
from django.shortcuts import render, redirect
from .models import Rents
from accounts.models import Accounts
from house.models import House
import datetime


def rent_view(request):
    if request.method == "GET":
        query_title = request.GET.get('title')
        house = House.objects.get(title=query_title)
        owner = house.created_by.username
        price = house.price
        date = (datetime.date.today())

        rent = Rents.objects.create(owner=owner, tenant=request.user,
                                    date_rented=date, last_payment_date=date, price=price, title=query_title)

    return render(request, "rent/detail.html", {'rent': rent})


# def rent_interested(request):
#     return render(request, '', {})


# def rent_confirmation(request):
#     return render(request, '', {})
