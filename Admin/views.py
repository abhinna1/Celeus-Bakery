from django.shortcuts import redirect, render
from Admin.forms import EditProductForm, ProductForm
from Product.models import Product
from Categories.models import Categories
from Basket.models import *
from Checkout.models import OrderShipping, ShippingInfo
from Product.models import Product

# Create your views here.

def AdminPanel(request):
    if request.user.is_superuser:
        shipping = OrderShipping.objects.all()
        return render(request, 'adminproducts.html', {'shipping': shipping})
    return redirect('/')

def adminViewOrder(request):
    if request.user.is_superuser:
        basketid = request.POST['basket']
        basket = Basket.objects.get(id = basketid)
        shipping = OrderShipping.objects.get(basket = basket)
        print('shipping address', shipping)

        print(basket)
        items = ItemBasket.objects.filter(basket_id = basket)
        sum = 0
        for i in items:
            sum = sum + i.product_id.price
        return render(request, 'adminvieworder.html', {'items': items, 'basket': basket, 'sum': sum, 'shipping': shipping})
    return redirect('/')

def adminviewProductList(request):
    if request.method=='GET':
        if request.user.is_superuser:
            products = Product.objects.all()
            return render(request, 'adminViewProducts.html', {'products': products})
    else:
        if request.user.is_superuser:
            id = request.POST['id']
            Product.objects.get(id=id).delete()
            products = Product.objects.all()
            return render(request, 'adminViewProducts.html', {'products': products, 'message': 'deleted'})
    return redirect('/')

def addProductAdminForm(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            print('form save')
            return redirect('/adminViewProduct')
    else:
        form = ProductForm()

    return render(request, 'adminAddProduct.html', {'form': form})


def editProductForm(request, product_id):
    prodDetail = Product.objects.get(id=product_id)

    if request.method == 'POST':
        print('in POST')
        form = ProductForm(request.POST, request.FILES, instance=prodDetail)
        if form.is_valid():
            form.save()
            print('form save')
            context={
                'prodDetail': prodDetail,
                'form':form,
                'message':'Product Updated'
            }
            return render(request,'editProductForm.html', context)


    else:
        print('in GET')
        form = ProductForm(instance=prodDetail)
    context={
        'prodDetail': prodDetail,
        'form':form,
    }

    return render(request,'editProductForm.html',context)


def toggledelivered(request, basket_id):
    basket = Basket.objects.get(id = basket_id)
    ordershipping = OrderShipping.objects.get(basket = basket)
    ordershipping.shippingInfo.is_delivered = not ordershipping.shippingInfo.is_delivered
    ordershipping.shippingInfo.save()
    return redirect('/adminorders')

def adminDeleteorderOrder(request):
    if request.method=='POST':
        basket = request.POST['basket_id']
        Basket.objects.get(id = basket).delete()