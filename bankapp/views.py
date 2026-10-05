from django.shortcuts import render


def home(request):
    return render(request, "bankapp/home.html")