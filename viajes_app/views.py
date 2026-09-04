from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def vista(request):
    return render(request, "viajes_core/vista.html")