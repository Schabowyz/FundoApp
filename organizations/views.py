from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Fundraise, Organization
from user.models import Connection, Notification

# Create your views here.


def search(request):
    return render(request, "organizations/search.html", {
        "notifications": Notification.getUserNotifications(request.user),
        "connections": Connection.getUserConnections(request.user),
        "orgs": Organization.objects.all()
    })


def organization(request, org_id):

    try:
        organization = Organization.objects.get(id=org_id)
    except:
        return redirect(reverse("base:not_found"))
    
    connections = Connection.getUserConnections(request.user)
    if connections:
        for connection in connections:
            if organization == connection.organization:
                user_org_relation = connection
                fundraises = Fundraise.getOrgsFundraises(organization)
    else:
        fundraises, user_org_relation = None, None

    return render(request, "organizations/organization.html", {
        "notifications": Notification.getUserNotifications(request.user),
        "connections": connections,
        "organization": organization,
        "user_org_relation": user_org_relation,
        "fundraises": fundraises
    })