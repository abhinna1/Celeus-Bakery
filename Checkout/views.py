import json
from urllib.request import Request
from MySQLdb import Date
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import ShippingInfo
from Basket.models import Basket, ItemBasket
from Register.models import User
from .models import OrderShipping
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.

@login_required(login_url='/login')
def orderProcess(request):
    userid = request.POST['user']
    basketid = request.POST['basket']
    
    phone = request.POST['phone']
    address = request.POST['address']
    
    basket = Basket.objects.get(id=basketid)
    user = User.objects.get(id=userid)
    basket.completed = True
    basket.save()
    shippingInfo = ShippingInfo.objects.create(basket = basket, user = user, phone = phone, address = address, order_date = datetime.date.today())
    shippingInfo.save()


    OrderShipping.objects.create(user = user, basket=basket, shippingInfo=ShippingInfo.objects.get(basket=basket)).save()
    return redirect('/order')

@login_required(login_url='/login')
def viewdetailorder(request):
    customer = request.user
    basketid = request.POST['basket']
    print('basket:::', basketid)

    basket = Basket.objects.get(id = basketid)

    print(basket)
    items = ItemBasket.objects.filter(basket_id = basket)
    sum = 0
    for i in items:
        sum = sum + i.product_id.price
    # return render(request, 'basket.html', {'ItemBasket': items, 'basket': basket})
    return render(request, 'detailOrder.html', {'items': items, 'basket': basket, 'sum': sum})

