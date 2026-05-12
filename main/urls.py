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
    path("galaxies/milky-way/", views.milky_way),
    path("galaxies/andromeda/", views.andromeda),
    path("galaxies/deep-space/", views.deep_space),
    path('galaxies/', views.galaxies, name='galaxies')
    
]