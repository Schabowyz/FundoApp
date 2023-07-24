from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

import os
from uuid import uuid4


# Helpers

def path_and_rename_organization(self, filename):
    upload_to = "images/organizations"
    ext = filename.split(".")[-1]
    filename = f"{uuid4().hex}.{ext}"
    return os.path.join(upload_to, filename)

def path_and_rename_fundraise(self, filename):
    upload_to = "images/fundraise"
    ext = filename.split(".")[-1]
    filename = f"{uuid4().hex}.{ext}"
    return os.path.join(upload_to, filename)



# Models


class Organization(models.Model):
    # Information
    name = models.CharField(max_length=128)
    description = models.CharField(blank=True, max_length=1024)
    webpage = models.URLField(blank=True, max_length=256)
    image = models.ImageField(blank=True, upload_to=path_and_rename_organization)

    # Settings
    currency_code = models.CharField(blank=False, max_length=3)
    budget = models.IntegerField()
    tokens_per_person = models.PositiveIntegerField(blank=False)


class OrganizationDomains(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    domain = models.URLField(max_length=256)


class Fundraise(models.Model):
    STATES = [
        ("ongoing", "ongoing"),
        ("finished", "finished")
    ]
    user = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=128)
    description = models.CharField(blank=True, max_length=1024)
    image = models.ImageField(blank=True, upload_to=path_and_rename_fundraise)
    state = models.CharField(choices=STATES, max_length=8)
    target_amount = models.PositiveIntegerField()
    current_amount = models.PositiveIntegerField()


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fundraise = models.ForeignKey(Fundraise, on_delete=models.SET_NULL, null=True)
    datetime = models.DateTimeField(default=timezone.now())
    tokens_amount = models.PositiveIntegerField()
    currency_code = models.CharField(blank=False, max_length=3)
    money_amount = models.PositiveIntegerField()


class Tokens(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)