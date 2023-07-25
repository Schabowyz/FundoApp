from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from organizations.models import Organization, Fundraise

# Create your models here.

class Connection(models.Model):
    RELATIONS = [
        ("owner", "owner"),
        ("employee", "employee")
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    relation = models.CharField(choices=RELATIONS, max_length=8)
    email = models.EmailField(max_length=256, unique=True)


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fundraise = models.ForeignKey(Fundraise, on_delete=models.SET_NULL, null=True)
    datetime = models.DateTimeField(default=timezone.now())
    seen = models.BooleanField(default=False)
    finished = models.BooleanField()