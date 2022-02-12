from cgi import print_directory
from django.shortcuts import redirect, render
from Product.models import Product
from .models import Basket, ItemBasket
from django.contrib.auth.decorators import login_required
from Categories.models import Categories


# Create your views here.
@login_required(login_url='/login')
def insertBasket(request, product_id):
    basket = Basket.objects.get_or_create(user_id_id = request.user.id, completed = False)
    product = Product.objects.get(id = product_id)
    # itembasket = ItemBasket.objects.filter(basket_id_id = basket[0].id)
    # data = Product.objects.get(id=product_id)
    # Basket.objects.create(user_id=request.user.id, product_id=data , quantity=1)
    ItemBasket.objects.create(product_id=product, basket_id=basket[0])
    return redirect('/basket')


@login_required(login_url='/login')
def removeBasket(request, id):
    # Basket.objects.get(id = basket_id).delete()
    ItemBasket.objects.get(id=id).delete()

    return redirect('/basket')

@login_required(login_url='/login')
def getBasket(request):
    basket = Basket.objects.get_or_create(user_id_id = request.user.id, completed = False)
    itembasket = ItemBasket.objects.filter(basket_id_id = basket[0].id)
    length = len(itembasket)
    return render(request, 'basket.html', {'ItemBasket': itembasket, 'length': length})