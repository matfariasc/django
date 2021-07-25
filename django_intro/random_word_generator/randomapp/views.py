from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.


class Contador(object):

    def __init__(self, inicial=0):
        self.numero = inicial

    def siguiente(self):
        self.numero += 1
        return self.numero

    def reset(self):
        self.numero = 0
        return self.numero


num = Contador()


def index(request):
    keys = get_random_string(length=14)
    contex = {
        "num": num.siguiente(),
        "key": keys

    }
    return render(request, "index.html", contex)


def random(request):
    keys = get_random_string(length=14)
    contex = {
        "num": num.siguiente(),
        "key": keys

    }
    return render(request, "index.html", contex)


def reset(request):
    num.reset()
    return redirect("/")
