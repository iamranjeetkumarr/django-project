from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def login(request):
    return render(request, "login.html")


def signup(request):
    return render(request, "signup.html")


def index(request):

    return render(request, "index.html")


def Portfolios(request):
    return render(request, "Portfolios.html")


def cybersecurity(request):
    return render(request, "cybersecurity.html")


def python(request):
    return render(request, "python.html")
