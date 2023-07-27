from django.shortcuts import render

from user.models import Connection, Notification

# Create your views here.


def index(request):
    return render(request, "base/index.html", {
        "notifications": Notification.getUserNotifications(request.user),
        "connections": Connection.getUserConnections(request.user)
    })


def about(request):
    return render(request, "base/about.html", {
        "notifications": Notification.getUserNotifications(request.user),
        "connections": Connection.getUserConnections(request.user)
    })


def not_found(request):
    return render(request, "base/not_found.html", {
        "notifications": Notification.getUserNotifications(request.user),
        "connections": Connection.getUserConnections(request.user)
    })