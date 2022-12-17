from django.shortcuts import render

from .models import House
from .forms import HouseForm
# Create your views here.


def house_create_view(request):
    if request.method == "GET":
        form = HouseForm(None)
    elif request.method == "POST":
        form = HouseForm(request.POST, request.FILES)
    context = {'form': form}
    if form.is_valid():
        obj = form.save()
        context['form'] = HouseForm()
        context['created'] = True
    return render(request, "house/create.html", context)


def house_detail_view(request, id):
    context = {}
    try:
        print('HERE')
        query = House.objects.get(id=id)
        print(query.option)
        if query.option == "TAKE RENT" or query.option == "GIVE RENT":
            context['rent'] = True
            print("HERE - 1")
        elif query.option == "BUY" or query.option == "SELL":
            context['sell'] = True
            print('HERE - 3')
        print("HERE - 4")
    except:
        query = None
    # print(query)
    context['object'] = query
    return render(request, "house/detail.html", context)
