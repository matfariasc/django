from typing import Pattern
from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('process_money', views.proccesmoney)
]
