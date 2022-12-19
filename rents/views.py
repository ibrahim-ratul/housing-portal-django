from django.shortcuts import render

from controllers.rents.controller import rent_view_controller


def rent_view(request):
    if request.method == "GET":
        query_title = request.GET.get('title')
        rent = rent_view_controller(query_title, request.user)

    return render(request, "rent/detail.html", {'rent': rent})
