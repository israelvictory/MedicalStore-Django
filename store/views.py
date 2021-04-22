from django.shortcuts import render, redirect
from .forms import CreateUserForm, LogUserForm, AddDealerForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import (
    Dealer, Medicine, Employee,
    Customer, Purchase,
)


def home_page(request):
    return render(request, "store/home.html")


@login_required
def logout_page(request):
    logout(request)
    return redirect("store:login")


def login_page(request):
    form = LogUserForm()

    if request.method == "POST":
        form = LogUserForm(request.POST)
        if form.is_valid():
            print(form)
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(
                request, username=username, password=password
            )

            if user is not None:
                login(request, user)
                messages.success(request, f"{username}, you are logged in.")
                return redirect("store:dashboard")
            messages.error(request, f"Oops, the username {username} does not exist in our database. Please try again.")
        return redirect("store:login")

    context = {
        'form': form
    }

    return render(request, "store/login.html", context)



def register_page(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has successfully been created.")
            return redirect("store:login")
        print("Something's not right.")
        return redirect("store:register")

    context = {
        'form': form
    }

    return render(request, "store/register.html", context)


@login_required
def dashboard_page(request):
    context = {

    }
    return render(request, "store/dashboard.html", context)


@login_required
def dealers_page(request):
    pass


@login_required
def add_dealer_page(request):
    form = AddDealerForm()

    if request.method == "POST":
        if form.is_valid():
            fname = form.cleaned_data.get("fname")
            lname = form.cleaned_data.get("lname")
            address = form.cleaned_data.get("address")
            phone_number = form.cleaned_data.get("phone_number")
            email = form.cleaned_data.get("email")
            print(fname, lname)

            dealer = Dealer(
                fname=fname, lname=lname, address=address,
                phone_number=phone_number, email=email
            )
            dealer.save()
            messages.success(request, "You have added a new dealer.")
            return redirect("store:view-dealers")
        return redirect("store:add-dealer")

    context = {
        'form': form
    }
    return render(request, "store/add-dealer.html", context)


@login_required
def medicines_page(request):
    pass


@login_required
def employees_page(request):
    pass


@login_required
def customers_page(request):
    pass


@login_required
def purchases_page(request):
    pass


@login_required
def confirm_logout_page(request):
    return render(request, "store/confirm-logout.html")


# @login_required
# def profile_page(request):
#     u_form = UpdateUserForm(instance=request.user)
#     p_form = UpdateProfileForm(instance=request.user.profile)

#     if request.method == "POST":
#         p_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
#         u_form = UpdateUserForm(instance=request.user, data=request.POST)

#         if p_form.is_valid() and u_form.is_valid():
#             username = u_form.cleaned_data.get("username")
#             p_form.user = username
#             p_form.save()
#             messages.success(request, f"{username}, you profile has successfully been updated.")
#             return redirect("note:profile")
#         return redirect("note:profile")

#     context = {
#         'p_form': p_form,
#         'u_form': u_form
#     }

#     return render(request, "note_frontend/profile.html", context)
