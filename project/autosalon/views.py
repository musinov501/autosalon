from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Cars, Brand

# Create your views here.

def home(request: HttpRequest):
    cars = Cars.objects.all()
    brands = Brand.objects.all()
    context = {
        'cars': cars,
        'brands': brands,
        'title': "Barcha mashinalar"
    }
    return render(request, "autosalon/index.html", context)


def cars_by_brand(request: HttpRequest, brand_id):
    cars = Cars.objects.filter(brand_id= brand_id)
    brands = Brand.objects.all()
    context = {
        'cars': cars,
        'brands': brands,
        'title': Brand.objects.get(pk = brand_id).name
    }
    return render(request, "autosalon/index.html", context)

def show_in_detail(request: HttpRequest, pk: int):
    brands = Brand.objects.all()
    car = Cars.objects.get(pk=pk)
    context = {
        'car': car,
        'brands': brands,
        'title': car.model
    }
    return render(request, 'autosalon/detail.html', context)