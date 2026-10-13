from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Asset(models.Model):

    ASSET_TYPES = [
        ("Laptop", "Laptop"),
        ("Monitor", "Monitor"),
        ("Keyboard", "Keyboard"),
        ("Headset", "Headset"),
    ]

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Assigned", "Assigned"),
        ("Rejected", "Rejected"),
    ]

    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    asset_type = models.CharField(
        max_length=20,
        choices=ASSET_TYPES
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    requested_on = models.DateTimeField(
        auto_now_add=True
    )

    assigned_on = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.employee.username} - {self.asset_type}"