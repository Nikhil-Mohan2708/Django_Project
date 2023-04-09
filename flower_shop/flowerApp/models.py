# Create your models here.
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.name


class Flower(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    availability = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='flowers/')
    description = models.TextField()
    stock = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-price']
        verbose_name_plural = 'Flowers'

    def __str__(self):
        return f'{self.color} {self.name} {self.category} ({self.price})'



