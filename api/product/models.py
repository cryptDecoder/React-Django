from django.db import models
from api.category.models import Category
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)
    stock = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True, blank=True, null=True)
    image = models.ImageField(
        upload_to='images/', blank=True, null=True)
    category = models.ForeignKey(
        Category, blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return "{:s}".format(self.name)
