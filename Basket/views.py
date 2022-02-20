from cgi import print_directory
from ctypes.wintypes import HRSRC
from datetime import date, datetime
from http.client import HTTPResponse
import json
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from Product.models import Product
from .models import Basket, ItemBasket
from django.contrib.auth.decorators import login_required
from Checkout.models import ShippingInfo, OrderShipping

# Create your views here.
@login_required(login_url='/login')
def insertBasket(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user
    product = Product.objects.get(id = productId)
    basket, created = Basket.objects.get_or_create(user_id = customer, completed = False)
    
    itemBasket, created = ItemBasket.objects.get_or_create(basket_id = basket, product_id = product)
    print(basket)
    print('basker:', itemBasket)
    # if action=='add':
    #     itemBasket.quantity = itemBasket.quantity+1
    if action=='addWithQty':
        itemBasket.quantity = itemBasket.quantity+1
    itemBasket.save()
    print('got data')

    print('productId:', productId, 'action:', action, 'qty: ' , 1)

    return JsonResponse('Hello', safe=False)

@login_required(login_url='/login')
def removeBasket(request):
    data = json.loads(request.body)
    # print(data)
    dataid = data['id']
    ItemBasket.objects.get(id = dataid).delete()
    # print(ItemBasket.objects.get(id=dataid))
    return JsonResponse('Item has been removed from basket.', safe=False)

@login_required(login_url='/login')
def getBasket(request):
    customer = request.user
    basket, created = Basket.objects.get_or_create(user_id = customer, completed = False)
    print(basket.id)
    items = basket.itembasket_set.all()
    return render(request, 'basket.html', {'ItemBasket': items, 'basket': basket})


def viewOrderlist(request):
    user = request.user

    if(user.is_authenticated):
        orders = OrderShipping.objects.filter(user = request.user)
                
    return render(request, 'OrderList.html', {'orders': orders})