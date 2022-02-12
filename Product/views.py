from django.forms import models
from django.shortcuts import redirect, render
from Product.models import Product
# Create your views here.
def viewProduct(request, product_id):
    data = Product.objects.get(id=product_id)
    return render(request, 'Product.html', {'data': data})
