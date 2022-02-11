from django.shortcuts import redirect, render
from Product.models import Product
from .models import Basket
from django.contrib.auth.decorators import login_required
from Categories.models import Categories


# Create your views here.
@login_required(login_url='/login')
def insertBasket(request, product_id):
    data = Product.objects.get(id=product_id)
    Basket.objects.create(user_id=request.user.id, product_id=data , quantity=1)
    return redirect('/basket')


@login_required(login_url='/login')
def removeBasket(request, basket_id):
    print('DATA::'  ,  basket_id)
    Basket.objects.get(id = basket_id).delete()

    return redirect('/basket')

@login_required(login_url='/login')
def getBasket(request):
    basketProducts = []
    basketCategory = []
    
    basket = Basket.objects.filter(user_id=request.user.id)
    for i in basket:
        basketProducts.append(i)
    for i in basketProducts:
        currentCategoryId = i.product_id.category_name_id
        currentCategory = Categories.objects.get(id = currentCategoryId)
        basketCategory.append(currentCategory)
     
    return render(request, 'basket.html', {'basketProducts': basketProducts, 'length': len(basketProducts)})