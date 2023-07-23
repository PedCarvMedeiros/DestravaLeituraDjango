from django.urls import path
from livros import views

app_name = "livros"

urlpatterns =[
    path("", views.livros, name="livros"),
]