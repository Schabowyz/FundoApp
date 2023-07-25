from django.shortcuts import render

# Create your views here.


def profile(reqeust, user_id):
    return render(reqeust, "user/profile.html", {
        "user_id": user_id
    })