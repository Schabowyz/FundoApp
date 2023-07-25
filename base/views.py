from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "base/index.html")


def about(reqeust):
    return render(reqeust, "base/about.html")


def not_found(request):
    return render(request, "base/not_found.html")