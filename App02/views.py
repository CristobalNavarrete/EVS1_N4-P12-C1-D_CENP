from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def vista1(request):
      return  HttpResponse("<h1 style> esta es la primera vista de la Rama App 02 </h1>"
                           "<h2 style> esta es la primera vista de la Rama App 02 </h2>"
                           "<h3 style> esta es la primera vista de la Rama App 02 </h3>"
                           "<h4 style> esta es la primera vista de la Rama App 02 </h4>"
                           "<ul>"
                            "<li>7</li>"
                            "<li>8</li>"
                            "<li>9</li>"
                            "</ul>")
def vista2(request):
            return  HttpResponse("<h1 style> esta es la Segunda vista de la Rama App 02 </h1>"
                           "<h2 style> esta es la Segunda vista de la Rama App 02 </h2>"
                           "<h3 style> esta es la Segunda vista de la Rama App 02 </h3>"
                           "<h4 style> esta es la Segunda vista de la Rama App 02 </h4>"
                           "<ul>"
                           "<li>10</li>"
                            "<li>11</li>"
                            "<li>12</li>"
                            "</ul>")