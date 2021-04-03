from django.db import models
import json
from django.utils.safestring import mark_safe
from django.conf import settings

# Create your models here.

class Category(models.Model):
    STATUS=(
        ("True","True"),
        ("False","False"),
        )

    parent=models.ForeignKey("self",
    on_delete=models.CASCADE, blank=True, null=True, related_name="children")

    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category/", blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS)
    slug = models.SlugField(unique=True, null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title


class Product(models.Model):
    status = (
        ('True', 'True'),
        ('False', 'False'),)
   
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='product/')
    new_price = models.PositiveIntegerField( default=0)
    old_price = models.PositiveIntegerField(default=0)
    amount = models.PositiveIntegerField(default=0)
    min_amount = models.IntegerField(default=3)
    
    detail = models.TextField()
    status = models.CharField(max_length=20, choices=status)
    slug = models.SlugField(null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title        

    def image_tag(self):
        return mark_safe('<img src="{}" heights="70" width="60" />'.format(self.image.url))
    image_tag.short_description = 'Image'

    def ImageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(blank=True, upload_to='product/')

    def __str(self):
        return self.title    