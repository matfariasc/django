from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    # sólo se envía todos los autores
    context = {"authors": Author.objects.all()}
    return render(request, "index.html", context)
