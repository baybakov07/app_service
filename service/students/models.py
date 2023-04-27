from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)


    def __str__(self):
        return f"Client: {self.first_name}"
