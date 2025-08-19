from django.db import models



class Brand(models.Model):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name



class Cars(models.Model):
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    engine = models.CharField(max_length=155)
    color = models.CharField(max_length=15)
    price = models.FloatField(max_length=15)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    review_video = models.FileField(upload_to="videos/", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    uploaded = models.BooleanField(default=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)


    def __str__(self):
        return self.model
