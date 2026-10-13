

# Register your models here.
from django.contrib import admin
from .models import Leave


@admin.register(Leave)
class LeaveAdmin(admin.ModelAdmin):

    list_display = (
        "employee",
        "leave_type",
        "start_date",
        "end_date",
        "status",
        "applied_on",
    )

    search_fields = (
        "employee__username",
        "reason",
    )

    list_filter = (
        "leave_type",
        "status",
        "start_date",
    )

    ordering = (
        "-applied_on",
    )