from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Cars, Brand

# Create your views here.

def home(request: HttpRequest):
    return HttpResponse('<h1 style= "color: green; text-align: center;">Assalomu alaykum Autasalonga Xush kelibsiz</h1>')


def cars(request: HttpRequest):
    automobiles = Cars.objects.all()

    context = {
        "automobiles": automobiles
    }

    return render(request, "autosalon/cars.html", context)


def brands(request: HttpRequest):
    cars_brands = Brand.objects.all()

    context = {
        "cars_brands": cars_brands
    }

    return render(request, "autosalon/brands.html", context)