from django.shortcuts import render

# Create your views here.


def search(request):
    return render(request, "organizations/search.html")


def organization(request, org_name):
    return render(request, "organizations/organization.html", {
        "org_name": org_name
    })