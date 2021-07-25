from typing import Hashable
from django.shortcuts import render, redirect, HttpResponse
import random
from time import gmtime, strftime

# Create your views here.


class gold(object):

    def __init__(self, inicial=0):
        self.numero = inicial
        self.list = []

    def ingreso(self, saldo):
        self.numero += saldo
        return self.numero

    def fram(self):
        win = random.randint(10, 20)
        oro.ingreso(win)
        times = strftime("%Y-%m-%d %H:%M %p", gmtime())
        dato = "Earned "+str(win) + \
            " golds from the farm! ("+times+")", "green"
        self.list.append(dato)
        return self.list

    def cave(self):
        win = random.randint(5, 10)
        oro.ingreso(win)
        times = strftime("%Y-%m-%d %H:%M %p", gmtime())
        dato = "Earned "+str(win) + \
            " golds from the cave! ("+times+")", "green"
        self.list.append(dato)
        return self.list

    def house(self):
        win = random.randint(2, 5)
        oro.ingreso(win)
        times = strftime("%Y-%m-%d %H:%M %p", gmtime())
        dato = "Earned "+str(win) + \
            " golds from the house! ("+times+")", "green"
        self.list.append(dato)
        return self.list

    def casino(self):
        win = random.randint(-50, 50)
        oro.ingreso(win)
        if 0 < win:
            times = strftime("%Y-%m-%d %H:%M %p", gmtime())
            dato = "Earned a casino and win "+str(win) + \
                " golds good look!!! ("+times+")", "green"
        elif 0 > win:
            times = strftime("%Y-%m-%d %H:%M %p", gmtime())
            dato = "Entered a casino and lost "+str(win) + \
                " golds ...... Ouch.. ("+times+")", "red"
        self.list.append(dato)
        return self.list


oro = gold()


def index(request):
    if request.method == "GET":
        datos = {
            'saldo': oro.numero,
            'registro': oro.list
        }
        print(oro.numero)
        print(oro.list)
        return render(request, "index.html", datos)


def proccesmoney(request):
    print("procesando")
    if request.method == "POST":
        tipo = request.POST["tipo"]
        if tipo == "fram":
            oro.fram()
        elif tipo == "cave":
            oro.cave()
        elif tipo == "house":
            oro.house()
        elif tipo == "casino":
            oro.casino()
    return redirect("/")
