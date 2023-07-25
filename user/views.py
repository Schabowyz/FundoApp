from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.


def profile(reqeust, user_id):
    try:
        user = User.objects.get(id=user_id)
    except:
        return redirect(reverse("base:not_found"))

    return render(reqeust, "user/profile.html", {
        "user": user
    })