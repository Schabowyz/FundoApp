from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Connection, Notification

# Create your views here.


def profile(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except:
        return redirect(reverse("base:not_found"))

    return render(request, "user/profile.html", {
        "notifications": Notification.getUserNotifications(request.user),
        "connections": Connection.getUserConnections(request.user),
        "user": user
    })