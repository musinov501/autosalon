from django.urls import path
from .views import home, cars_by_brand, show_in_detail

urlpatterns = [
    path('', home, name = "home"),
    path('brand/<int:brand_id>/', cars_by_brand, name = 'by_brand'),
    path('cars/<int:pk>/', show_in_detail, name = 'detail' )

]
