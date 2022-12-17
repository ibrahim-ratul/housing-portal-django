from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import House
from .forms import HouseForm


@login_required
def house_create_view(request):
    context = {}
    if request.method == "GET" and request.user.is_owner:
        form = HouseForm(None)
    elif request.method == "POST" and request.user.is_owner:
        form = HouseForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user
            obj.save()
            context['form'] = HouseForm()
            context['created'] = True
            context['object'] = obj
            return redirect('home')
    else:
        return redirect('home')
    context = {'form': form}
    return render(request, "house/create.html", context)


def house_detail_view(request, id):
    context = {}
    try:
        query = House.objects.get(id=id)
        context['object'] = query
    except:
        query = None
    context['object'] = query
    return render(request, "house/detail.html", context)


def house_search_view(request):
    query_dict = request.GET  # This is a dictionary
    try:
        query = query_dict.get("q")
    except:
        query = None
    house_objects = None
    if query is not None:
        try:
            house_objects = House.objects.filter(price__lte=query)
        except Exception as e:
            house_objects = House.objects.filter(address__icontains=query)
        except:
            house_objects = None
    context = {
        "house_objects": house_objects,
    }
    return render(request, "house/search.html", context=context)
