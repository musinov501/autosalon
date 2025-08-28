from django.contrib import admin
from .models import Brand, Cars

# Register your models here.

admin.site.register(Brand)


class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price', 'updated')
    search_fields = ('model', 'color', 'brand')
    fieldsets = (
        ("Basic Information", {
            "fields": ("brand", "model", "year", "color"),
            "description": "Asosiy ma’lumotlarni shu yerga kiriting"
        }),
        ("Technical Details", {
            "fields": ("engine", "price", "image"),
            "description": "Bu yerda dvigatel xususiyatlarini, narxini va ixtiyoriy rasmini qo‘shing"
        }),
        ("Dates", {
            "fields": ("created", "updated", "uploaded")
        })
    )
    readonly_fields = ("created", "updated")
    date_hierarchy = "created"


admin.site.register(Cars, CarAdmin)
