from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import HouseForm
from controllers.house.controller import house_detail_controller, house_search_controller


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
            return redirect('home')
    else:
        return redirect('home')
    context = {'form': form}
    return render(request, "house/create.html", context)


def house_detail_view(request, slug):
    context = house_detail_controller(slug)
    context['is_tenant'] = request.user.is_tenant

    return render(request, "house/detail.html", context)


def house_search_view(request):
    query_dict = request.GET
    context = house_search_controller(query_dict)

    return render(request, "house/search.html", context=context)
