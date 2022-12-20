from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, AccountUpdateForm
from controllers.accounts.controller import profile_controller, profile_view_controller


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
    else:
        form = AuthenticationForm(request)
    context = {"form": form}
    return render(request, "accounts/login.html", context)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    return render(request, "accounts/logout.html", {})


def register_view(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save(commit=False)
        user_obj.user = request.user
        user_obj.save()

        return redirect("/login")
    context = {"form": form}
    return render(request, "accounts/register.html", context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = AccountUpdateForm(
            request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = AccountUpdateForm(instance=request.user)
    context = {
        'account': request.user,
        'form': form
    }

    context.update(profile_controller(request.user))

    return render(request, 'accounts/profile.html', context)


@login_required
def profile_view(request, username=None):
    if username is not None:
        context = profile_view_controller(username)
        return render(request, 'accounts/profile.html', context)

    return redirect('home')
