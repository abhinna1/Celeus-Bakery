from django.db import models
from Categories.models import Categories
# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to = 'Product_Images')
    category_name = models.ForeignKey(Categories, on_delete=models.CASCADE)
    def __str__(self):
        return self.product_name