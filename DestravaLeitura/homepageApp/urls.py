from django.urls import path
from homepageApp import views

app_name = "homepageApp"

urlpatterns =[
    path("", views.homepage, name="homepage"),
    path("sobre/", views.sobre, name="sobre")
]