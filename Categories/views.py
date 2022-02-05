from django.shortcuts import redirect, render
from .models import Categories
from Product.models import Product
# Create your views here.

def categoryPage(request):
    id = request.GET['id']
    category = Categories.objects.get(id = id)
    data = Product.objects.filter(category_name_id = id)
    return render(request, 'categoryPage.html', {'data':data, 'category': category})

def viewProduct(request):
    return redirect(request, '/product?id=1')