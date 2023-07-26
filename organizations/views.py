from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Fundraise, Organization
from user.models import Connection

# Create your views here.


def search(request):
    return render(request, "organizations/search.html", {
        "orgs": Organization.objects.all()
    })


def organization(request, org_id):
    context = {}

    try:
        context["org"] = Organization.objects.get(id=org_id)
    except:
        return redirect(reverse("base:not_found"))
    
    context["connection"] = Connection.objects.filter(user=request.user, organization=context["org"])
    
    if context["connection"].exists():
        context["connection"] = context["connection"][0]
        context["fundraises"] = {
            "ongoing": Fundraise.objects.filter(organization=context["org"], state="ongoing"),
            "finished": Fundraise.objects.filter(organization=context["org"], state="finished")
        }

    return render(request, "organizations/organization.html", context)