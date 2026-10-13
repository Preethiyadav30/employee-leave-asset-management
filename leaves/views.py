from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import LeaveForm
from .models import Leave
from django.contrib.admin.views.decorators import staff_member_required


@login_required
def apply_leave(request):

    if request.method == "POST":

        form = LeaveForm(request.POST)

        if form.is_valid():

            leave = form.save(commit=False)

            leave.employee = request.user

            leave.save()

            return redirect("leave_history")

    else:
        form = LeaveForm()

    return render(
        request,
        "leaves/apply_leave.html",
        {"form": form}
    )

@login_required
def leave_history(request):

    leaves = Leave.objects.filter(
        employee=request.user
    ).order_by("-applied_on")

    return render(
        request,
        "leaves/leave_history.html",
        {"leaves": leaves}
    )


@login_required
def cancel_leave(request, leave_id):

    leave = Leave.objects.get(
        id=leave_id,
        employee=request.user
    )

    if leave.status == "Pending":

        leave.status = "Cancelled"
        leave.save()

    return redirect("leave_history")


@staff_member_required
def manage_leaves(request):

    leaves = Leave.objects.all().order_by("-applied_on")

    return render(
        request,
        "leaves/manage_leaves.html",
        {"leaves": leaves}
    )

@staff_member_required
def approve_leave(request, leave_id):

    leave = Leave.objects.get(id=leave_id)

    if leave.status == "Pending":
        leave.status = "Approved"
        leave.save()

    return redirect("manage_leaves")


@staff_member_required
def reject_leave(request, leave_id):

    leave = Leave.objects.get(id=leave_id)

    if leave.status == "Pending":
        leave.status = "Rejected"
        leave.save()

    return redirect("manage_leaves")