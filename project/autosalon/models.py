from django.db import models



class Brand(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Brend"
        verbose_name_plural = "Brendlar"



class Cars(models.Model):
    model = models.CharField(max_length=100, verbose_name="Mashina modeli")
    year = models.IntegerField(verbose_name="Mashina chiqarilgan yil")
    engine = models.CharField(max_length=155, verbose_name="Mashina motori")
    color = models.CharField(max_length=15, verbose_name="Mashina rangi")
    price = models.FloatField(max_length=15, verbose_name="Mashina narxi")
    description = models.TextField(null=True, blank=True, verbose_name="Ma'lumot")
    image = models.ImageField(upload_to="images/", null=True, blank=True, verbose_name="Rasmi")
    review_video = models.FileField(upload_to="videos/", null=True, blank=True, verbose_name="Videosi")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    uploaded = models.BooleanField(default=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Brendi")


    def __str__(self):
        return self.model

    class Meta:
        verbose_name = "Mashina"
        verbose_name_plural = "Mashinalar"
        ordering = ['id']
