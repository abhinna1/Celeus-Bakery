from django import forms

from Product.models import Product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name','price','category_name','description','image')

class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('product_name','price','category_name','description','image')
