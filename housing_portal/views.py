from django.shortcuts import render

from house.models import House


def home_view(request):
    house_list = House.objects.all()
    context = {"object_list": house_list}
    return render(request, "home.html", context)
