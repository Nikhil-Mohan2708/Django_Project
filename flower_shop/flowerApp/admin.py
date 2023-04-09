# Register your models here.
from django.contrib import admin
from .models import Category, Flower


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category,CategoryAdmin)


class FlowerAdmin(admin.ModelAdmin):
    list_display = ('color', 'category', 'price','stock', 'availability')
    list_filter = ('category', 'color', 'price')
    list_editable = ['price', 'stock', 'availability']
    search_fields = ('color', 'category__name')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Flower,FlowerAdmin)
