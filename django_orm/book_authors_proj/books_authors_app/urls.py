from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books/<int:number>', views.view_book),
    path('author', views.author),
    path('author/<int:number>', views.view_author),
]
