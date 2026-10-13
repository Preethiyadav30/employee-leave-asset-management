from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Asset


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):

    list_display = (
        "employee",
        "asset_type",
        "status",
        "requested_on",
        "assigned_on",
    )

    search_fields = (
        "employee__username",
        "asset_type",
    )

    list_filter = (
        "asset_type",
        "status",
        "requested_on",
    )

    ordering = (
        "-requested_on",
    )
