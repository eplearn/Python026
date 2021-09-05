from django.urls import path
from . import views

urplpatterns = [
    path('', views.index)
]
