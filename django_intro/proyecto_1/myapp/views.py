from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def root(request):
    return redirect("/")
