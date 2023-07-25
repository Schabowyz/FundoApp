from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Fundraise, Organization

# Create your views here.


def search(request):
    return render(request, "organizations/search.html", {
        "orgs": Organization.objects.all()
    })


def organization(request, org_id):
    try:
        org = Organization.objects.get(id=org_id)
    except:
        return redirect(reverse("base:not_found"))
    
    fundraises = {
        "ongoing": Fundraise.objects.filter(organization=org, state="ongoing"),
        "finished": Fundraise.objects.filter(organization=org, state="finished")
    }
    
    return render(request, "organizations/organization.html", {
        "org": org,
        "fundraises": fundraises
    })