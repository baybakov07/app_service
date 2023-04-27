from django.contrib.auth.models import User
from django.db import models


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    balance = models.DecimalField(decimal_places=2, max_digits=10, default=0)

    def __str__(self):
        return self.user.username
