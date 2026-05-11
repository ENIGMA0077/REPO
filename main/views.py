from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def galaxies(request):
    return render(request, "galaxies.html")