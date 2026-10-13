

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Leave(models.Model):

    LEAVE_TYPES = [
        ("Sick", "Sick Leave"),
        ("Casual", "Casual Leave"),
        ("Earned", "Earned Leave"),
    ]

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Rejected", "Rejected"),
        ("Cancelled", "Cancelled"),
    ]

    employee = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    leave_type = models.CharField(
        max_length=20,
        choices=LEAVE_TYPES
    )

    start_date = models.DateField()

    end_date = models.DateField()

    reason = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    applied_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.employee.username} - {self.leave_type}"