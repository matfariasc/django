from django.shortcuts import render, HttpResponse, redirect

# Create your views here.


def index(request):
    if request.method == "GET":
        print("a GET request is being made to this route")
        return render(request, "index.html")
    if request.method == "POST":
        val_from_field_one = request.POST["one"]
        val_from_field_two = request.POST["two"]
        print("a POST request is being made to this route")
        return redirect("/")

# def index(request):
#     context = {
#         "name": "Noelle",
#         "favorite_color": "turquoise",
#         "pets": ["Bruce", "Fitz", "Georgie"]
#     }
#     return render(request, "index.html", context)
