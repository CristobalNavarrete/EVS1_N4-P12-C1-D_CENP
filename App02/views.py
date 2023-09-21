from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def vista1(request):
      return  HttpResponse("<h1> esta es la primera vista de la Rama App 02 </h1>")
def vista2(request):
      return  HttpResponse("<h1> esta es la segunda vista de la Rama App 02 </h1>")