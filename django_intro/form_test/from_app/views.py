from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, "index.html")


def create_user(request):
    # esta es la ruta que procesa form
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    context = {
        "name_on_template": name_from_form,
        "email_on_template": email_from_form
    }
    return redirect("/success")


def success(request):
    # esta es la ruta de éxito
    return render(request, "success.html")
