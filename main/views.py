from django.shortcuts import render

def home(request):
    return render(request, "main/home.html")

def galaxies(request):
    return render(request, "main/galaxies.html")