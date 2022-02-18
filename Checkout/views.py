import json
from urllib.request import Request
from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import ShippingInfo
from Basket.models import Basket
from Register.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login')
def orderProcess(request):
    # data = json.loads(request.body)
    print('in orderProcess URL')
    userid = request.POST['user']
    basketid = request.POST['basket']
    
    phone = request.POST['phone']
    address = request.POST['address']
    
    print('USER ID:: ', userid)
    basket = Basket.objects.get(id=basketid)
    user = User.objects.get(id=userid)
    basket.completed = True
    basket.save()
    shippingInfo = ShippingInfo.objects.create(basket = basket, user = user, phone = phone, address = address)
    shippingInfo.save()
    return redirect('/login')