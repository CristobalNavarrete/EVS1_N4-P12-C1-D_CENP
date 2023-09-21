from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def vista1(request):
      return  HttpResponse("<h1 style> esta es la primera vista de la Rama App 01 </h1>"
                           "<h2 style> esta es la primera vista de la Rama App 01 </h2>"
                           "<h3 style> esta es la primera vista de la Rama App 01 </h3>"
                           "<h4 style> esta es la primera vista de la Rama App 01 </h4>"
                           "<ul>"
                            "<li>1</li>"
                            "<li>2</li>"
                            "<li>3</li>"
                            "</ul>")
def vista2(request):
            return  HttpResponse("<h1 style> esta es la Segunda vista de la Rama App 01 </h1>"
                           "<h2 style> esta es la Segunda vista de la Rama App 01 </h2>"
                           "<h3 style> esta es la Segunda vista de la Rama App 01 </h3>"
                           "<h4 style> esta es la Segunda vista de la Rama App 01 </h4>"
                           "<ul>"
                           "<li>4</li>"
                            "<li>5</li>"
                            "<li>6</li>"
                            "</ul>")