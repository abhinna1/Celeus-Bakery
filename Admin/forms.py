from django import forms

from Product.models import Product
from Basket.models import ItemBasket
from Checkout.models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name','price','category_name','description','image')

class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name','price','category_name','description','image')

class EditOrderForm(forms.ModelForm):
    class Meta:
        shipping = ItemBasket
        fields = ('basket_id','product_id','quantity')