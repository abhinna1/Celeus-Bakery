"""bakery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Admin.views import *
from Basket.models import Basket
from Login.views import *
from Basket.views  import *
from django.conf import settings
from django.conf.urls. static import static
from Checkout.views import *
from Home.views import AboutPage, ServicesPage, homepage
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('login/', include('Login.urls'), name='login'),
    path('register/', include('Register.urls'), name='register'),
    path('logout/', Acclogout),
    path('product/', include('Product.urls'), name='product'),
    path('category/', include('Categories.urls')),
    path('basket/', include('Basket.urls')),
    path('update_item/', insertBasket, name='update_item'),
    path('removebasket/', removeBasket, name='remove_basket'),
    path('incrementBasketProduct/', incrementBasketProduct, name='incrementBasketProduct'),
    path('decrementBasketProduct/', decrementBasketProduct, name='decrementBasketProduct'),
    path('orderProcess/', orderProcess, name='orderProcess'),
    path('order/', viewOrderlist, name='orderlist'),
    path('vieworder/', viewdetailorder, name='vieworder'),
    path('adminorders/', AdminPanel, name='adminorders'),
    path('adminvieworder/', adminViewOrder, name='adminvieworder'),
    path('adminViewProduct/', adminviewProductList, name='adminViewProduct'),
    path('addProductForm/', addProductAdminForm, name='addProductForm'),
    path('editProductForm/<int:product_id>', editProductForm, name='editProductForm'),
    path('toggledelivered/<int:basket_id>', toggledelivered, name='toggledelivered'),
    path('adminDeleteorderOrder/', adminDeleteorderOrder, name='adminDeleteorderOrder'),
    path('about/', AboutPage, name='about'),
    path('services/', ServicesPage, name='services'),

    



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)