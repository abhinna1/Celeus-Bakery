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
from Admin.views import AdminPanel
from Basket.models import Basket
from Login.views import *
from Basket.views  import *
from django.conf import settings
from django.conf.urls. static import static
from Checkout.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('Login.urls')),
    path('register/', include('Register.urls')),
    path('logout/', Acclogout),
    path('product/', include('Product.urls')),
    path('category/', include('Categories.urls')),
    path('basket/', include('Basket.urls')),
    path('update_item/', insertBasket, name='update_item'),
    path('removebasket/', removeBasket, name='remove_basket'),
    path('orderProcess/', orderProcess, name='orderProcess'),
    path('order/', viewOrderlist, name='orderlist'),
    path('vieworder/', viewdetailorder, name='vieworder'),
    path('adminproducts/', AdminPanel, name='adminproduct'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)