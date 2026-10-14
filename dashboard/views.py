from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from leaves.models import Leave


@login_required
def dashboard(request):

    total_employees = User.objects.filter(
        is_staff=False,
        is_superuser=False
    ).count()

    pending_leaves = Leave.objects.filter(
        status="Pending"
    ).count()

    approved_leaves = Leave.objects.filter(
        status="Approved"
    ).count()

    rejected_leaves = Leave.objects.filter(
        status="Rejected"
    ).count()

    context = {
        "total_employees": total_employees,
        "pending_leaves": pending_leaves,
        "approved_leaves": approved_leaves,
        "rejected_leaves": rejected_leaves,
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )
