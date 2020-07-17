from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(max_length=255,unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name        = models.CharField(max_length=255,unique=True)
    slug        = models.SlugField(max_length=255,unique=True)
    description = models.TextField(blank=True)
    price       = models.DecimalField(max_digits=10,decimal_places=2)
    category    = models.ForeignKey(Category,on_delete=models.CASCADE)
    image       = models.ImageField(upload_to="product",blank=True)
    stock       = models.IntegerField()
    available   = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name