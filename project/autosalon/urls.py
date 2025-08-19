from django.urls import path
from .views import home, cars, brands


urlpatterns = [
    path('', home, name = "home"),
    path('cars/', cars, name = "cars"),
    path('brands/', brands, name= "brands")
]
