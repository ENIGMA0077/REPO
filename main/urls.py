from django.urls import path
from . import views



urlpatterns = [
    path('', views.home),
    path("article/black-holes/", views.black_holes),
    path("article/dark-matter/", views.dark_matter),
    path("article/quantum/", views.quantum),
    path("article/micro-world/", views.micro),
    path("article/macro-world/", views.macro),
    path("article/environment/", views.environment),
    path('galaxies/', views.galaxies, name='galaxies'),
]