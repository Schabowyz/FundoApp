from django.urls import path

from . import views


app_name = "user"
urlpatterns = [
    path("<user_id>", views.profile, name="profile")
]