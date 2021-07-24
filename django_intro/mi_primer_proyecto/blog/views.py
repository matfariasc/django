from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def root(request):
    return redirect('/blogs')


def index(request):
    return HttpResponse("Placeholder para luego mostrar una lista de todos los blogs")


def new(request):
    return HttpResponse("Placeholder para mostar un nuevo formulario para crear un nuevo blog")


def create(request):
    return redirect("/")


def show(request, number):
    return HttpResponse(f"Placeholder para mostar blogs numero: {number}")


def edit(request, number):
    return HttpResponse(f"Placerholder para editar el blog {number}")


def destroy(request, number):
    return redirect("/")
