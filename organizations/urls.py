from django.urls import path

from . import views

app_name="organizations"
urlpatterns = [
    path("", views.search, name="search"),
    path("<org_name>", views.organization, name="organization")
]