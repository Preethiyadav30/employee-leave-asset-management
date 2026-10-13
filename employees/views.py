from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import EmployeeProfileForm

# Create your views here.
@login_required
def profile(request):

    employee= Employee.objects.get(user=request.user)

    return render(request,"employees/profile.html",{"employee":employee})


@login_required
def edit_profile(request):

    employee = Employee.objects.get(user=request.user)

    if request.method == "POST":

        form = EmployeeProfileForm(
            request.POST,
            request.FILES,
            instance=employee
        )

        if form.is_valid():
            form.save()
            return redirect("profile")

    else:
        form = EmployeeProfileForm(instance=employee)

    return render(
        request,
        "employees/edit_profile.html",
        {"form": form}
    )