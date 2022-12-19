from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, AccountUpdateForm
from .models import Accounts


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
        p_form = AccountUpdateForm(
            request.POST, request.FILES, instance=request.user)

        if p_form.is_valid():
            p_form.save()
            messages.success(
                request, f'Your Account has been updated!')
            return redirect('profile')
    else:
        p_form = AccountUpdateForm(instance=request.user)

    context = {
        'account': request.user,
        'p_form': p_form
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def profile_view(request, username=None):
    if username is not None:
        try:
            user = Accounts.objects.get(username=username)
        except:
            user = None

        context = {
            'view': True,
            'account': user
        }
        return render(request, 'accounts/profile.html', context)
    return redirect('home')
