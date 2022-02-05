from django.forms import models
from django.shortcuts import redirect, render
from Product.models import Product
# Create your views here.
def viewProduct(request):
    id = request.GET['id']
    data = Product.objects.get(id=id)
    return render(request, 'Product.html', {'data':data})
