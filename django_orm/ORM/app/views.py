from django.shortcuts import render, HttpResponse
from .models import Movie

# Create your views here.


def index(request):
    context = {
        "all_the_movies": Movie.objects.all()
    }
    return render(request, "index.html", context)
