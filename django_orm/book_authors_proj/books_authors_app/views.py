from django.shortcuts import render, redirect
from . import models

# Create your views here.


def index(request):
    if request.method == "GET":
        datos = {
            'books': models.book.objects.all(),
        }
        return render(request, "index.html", datos)
    if request.method == "POST":
        titulo = request.POST['titulo']
        descripcion = request.POST['descripcion']
        print(titulo, "*" * 10, descripcion)
        models.book.objects.create(title=titulo, desc=descripcion)
        datos = {
            'books': models.book.objects.all(),
        }
        return render(request, "index.html", datos)


def view_book(request, number):
    if request.method == "GET":
        datos = {
            'books': models.book.objects.get(id=number),
            'authors': models.author.objects.all()
        }
        return render(request, "view_book.html", datos)
    if request.method == "POST":
        id_author = request.POST['author']
        print(id_author, "*" * 10, number)
        this_book = models.book.objects.get(id=number)
        this_author = models.author.objects.get(id=id_author)
        this_author.books.add(this_book)
        datos = {
            'books': models.book.objects.get(id=number),
            'authors': models.author.objects.all()
        }
        return render(request, "view_book.html", datos)


def author(request):
    if request.method == "GET":
        datos = {
            'authors': models.author.objects.all(),
        }
        return render(request, "authors.html", datos)
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        notes = request.POST['notes']
        models.author.objects.create(first_name=fname,
                                     last_name=lname,
                                     notas=notes)
        datos = {
            'authors': models.author.objects.all(),
        }
        return render(request, "authors.html", datos)


def view_author(request, number):
    if request.method == "GET":
        datos = {
            'books': models.book.objects.all(),
            'authors': models.author.objects.get(id=number)
        }
        return render(request, "view_author.html", datos)
    if request.method == "POST":
        id_book = request.POST['book']
        this_book = models.book.objects.get(id=id_book)
        this_author = models.author.objects.get(id=number)
        this_author.books.add(this_book)
        datos = {
            'books': models.book.objects.all(),
            'authors': models.author.objects.get(id=number)
        }
        return render(request, "view_author.html", datos)
