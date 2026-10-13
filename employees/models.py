from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    profile_photo = models.ImageField(
        upload_to='profile_photos/',
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username