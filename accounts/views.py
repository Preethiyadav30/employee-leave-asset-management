from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from employees.models import Employee
from .forms import RegistrationForm,LoginForm
from django.contrib.auth.decorators import login_required


def register(request):

    if request.method == "POST":

        form = RegistrationForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            department = form.cleaned_data["department"]
            phone = form.cleaned_data["phone"]

            user = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password
            )

            Employee.objects.create(
                user=user,
                department=department,
                phone=phone
            )

            return redirect("login")

    else:
        form = RegistrationForm()

    return render(request, "accounts/register.html", {"form": form})

def login_view(request):

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:

                employee = Employee.objects.get(user=user)

                if not employee.is_active:
                    form.add_error(
                        None,
                        "Your account has been disabled. Please contact the administrator."
                    )
                else:
                    login(request, user)
                    return redirect("profile")

            else:
                form.add_error(
                    None,
                    "Invalid username or password."
                )

    else:
        form = LoginForm()

    return render(
        request,
        "accounts/login.html",
        {"form": form}
    )

def logout_view(request):
    logout(request)
    return redirect("login")

