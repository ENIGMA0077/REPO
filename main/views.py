from django.shortcuts import render

def home(request):
    return render(request, "main/home.html")

def environment(request):
    return render(request, "main/article_environment.html")

def black_holes(request):
    return render(request, "main/article_black_holes.html")

def dark_matter(request):
    return render(request, "main/article_dark_matter.html")

def quantum(request):
    return render(request, "main/article_quantum.html")

def micro(request):
    return render(request, "main/article_micro.html")

def macro(request):
    return render(request, "main/article_macro.html")

def milky_way(request):
    return render(request, "galaxies/milky_way.html")

def andromeda(request):
    return render(request, "galaxies/andromeda.html")

def deep_space(request):
    return render(request, "galaxies/deep_space.html")

def galaxies(request):
    return render(request, 'main/galaxies.html')


def article(request, slug):
    articles = {
        "black-holes": {
            "title": "Black Holes",
            "content": """
A black hole is a region of spacetime where gravity is so strong that nothing can escape from it, not even light.

They form when massive stars collapse at the end of their life cycle.

Interesting fact:
If you fall into a black hole, time slows down relative to outside observers.
"""
        },

        "dark-matter": {
            "title": "Dark Matter",
            "content": """
Dark matter is invisible matter that does not emit light or energy.

It makes up about 85% of all matter in the universe.

Interesting fact:
Without dark matter, galaxies would fly apart instead of holding their shape.
"""
        },

        "dna": {
            "title": "DNA",
            "content": """
DNA (Deoxyribonucleic Acid) contains the genetic instructions for all living organisms.

It is made of four bases: A, T, C, G.

Interesting fact:
If stretched, DNA from one human cell would be about 2 meters long.
"""
        },

        "quantum": {
            "title": "Quantum Physics",
            "content": """
Quantum physics describes the behavior of matter and energy at atomic and subatomic levels.

Particles can exist in multiple states at once (superposition).

Interesting fact:
Observation can change the state of a quantum particle.
"""
        }
    }

    data = articles.get(slug, {
        "title": "Not Found",
        "content": "Article not found."
    })

    return render(request, "main/article.html", data)
