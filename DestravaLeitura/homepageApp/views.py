from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Ola")

def homepage(request):
    return render(request, "homepageApp/homepage.html")

def sobre(request):
    return render(request, "homepageApp/sobre.html")